from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from utils.states import FeedbackState
from keyboards.inline import get_feedback_keyboard
from utils.database import add_user_feedback, update_user_step


router = Router()

@router.message(lambda message: message.text == "Отзыв")
async def start_feedback_handler(message: types.Message):
    await message.answer("Нажмите кнопку, чтобы оставить отзыв.", reply_markup=get_feedback_keyboard())

@router.callback_query(lambda callback: callback.data == "feedback")
async def process_feedback_button(callback: types.CallbackQuery, state: FSMContext):
      await callback.message.answer("Пожалуйста, напишите ваш отзыв:")
      await update_user_step(callback.from_user.id, FeedbackState.FEEDBACK)
      await callback.answer()

@router.message(FeedbackState.FEEDBACK)
async def process_feedback(message: types.Message, state: FSMContext):
      user_id = message.from_user.id
      feedback = message.text
      add_user_feedback(user_id, feedback)
      await message.answer("Спасибо за ваш отзыв!")
      await state.clear()
      await update_user_step(user_id, None)