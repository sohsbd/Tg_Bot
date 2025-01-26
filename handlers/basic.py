from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from keyboards.reply import get_main_keyboard
from utils.database import add_user, get_user, update_user_step, create_user_data_file
from utils.states import RegistrationState

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: types.Message):
    create_user_data_file()
    user_id = message.from_user.id
    user = get_user(user_id)
    if user and user['registered']:
          await message.answer(f"Добро пожаловать, {user['first_name']}! Вы уже зарегистрированы.", reply_markup=get_main_keyboard())
    else:
        await message.answer("Здравствуйте! Давайте зарегистрируемся. Пожалуйста, введите ваше имя:")
        await update_user_step(user_id, RegistrationState.GET_NAME)

@router.message(Command("menu"))
async def command_menu_handler(message: types.Message):
    user_id = message.from_user.id
    user = get_user(user_id)
    if user and user['registered']:
          await message.answer("Выберите действие из меню:", reply_markup=get_main_keyboard())

@router.message(lambda message: message.text == "Информация о заболеваниях")
async def info_handler(message: types.Message):
    await message.answer("Здесь будет информация о сердечных заболеваниях.")

@router.message(lambda message: message.text == "Рекомендации")
async def recommendations_handler(message: types.Message):
    await message.answer("Здесь будут рекомендации по образу жизни.")