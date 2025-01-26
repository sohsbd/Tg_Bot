import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import basic, registration, questionnaire, llm_interaction, feedback
from middlewares import registration_check, user_log
from utils.reminder import setup_reminders


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Регистрация мидлваров
    dp.message.middleware(user_log.UserLogMiddleware())
    dp.callback_query.middleware(user_log.UserLogMiddleware())
    dp.message.middleware(registration_check.RegistrationCheckMiddleware())
    dp.callback_query.middleware(registration_check.RegistrationCheckMiddleware())

    # Регистрация роутеров
    dp.include_router(basic.router)
    dp.include_router(registration.router)
    dp.include_router(questionnaire.router)
    dp.include_router(llm_interaction.router)
    dp.include_router(feedback.router)

    # Запуск напоминаний
    scheduler = await setup_reminders(bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        scheduler.shutdown(wait=False)


if __name__ == "__main__":
    asyncio.run(main())