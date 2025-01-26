from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot

async def send_reminder(bot: Bot, user_id: int, text: str):
  """Отправляет напоминание пользователю."""
  await bot.send_message(user_id, text)

async def setup_reminders(bot: Bot):
    """Инициализирует планировщик задач для напоминаний."""
    scheduler = AsyncIOScheduler()
    # Добавляйте задачи в scheduler.add_job()
    # Например, напоминания через каждый день:
    # all_user_ids = get_all_registered_users()
    # for user_id in all_user_ids:
    #     scheduler.add_job(send_reminder, 'interval', days=1, args=[bot, user_id, "Не забудьте принять лекарства!"])
    scheduler.start()
    return scheduler