from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from utils.states import RegistrationState
from utils.database import update_user, update_user_step, get_user
from keyboards.reply import get_main_keyboard

router = Router()

@router.message(RegistrationState.GET_NAME)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await message.answer("Теперь введите вашу фамилию:")
    await update_user_step(message.from_user.id, RegistrationState.GET_LAST_NAME)

@router.message(RegistrationState.GET_LAST_NAME)
async def process_last_name(message: types.Message, state: FSMContext):
     await state.update_data(last_name=message.text)
     data = await state.get_data()
     first_name = data["first_name"]
     last_name = data["last_name"]
     user_id = message.from_user.id
     update_user(user_id, {'registered': True, 'first_name': first_name, 'last_name': last_name})
     await message.answer(f"Регистрация завершена! Добро пожаловать, {first_name} {last_name}!", reply_markup=get_main_keyboard())
     await state.clear()
     await update_user_step(user_id, None)