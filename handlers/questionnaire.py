from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from keyboards.inline import get_questionnaire_keyboard
from utils.states import QuestionnaireState
from utils.database import update_user_questionnaire_step, update_user
import json

router = Router()

questions = [
    "Вопрос 1: Как часто вы испытываете боли в груди?",
    "Вопрос 2: Есть ли у вас одышка при физической нагрузке?",
    "Вопрос 3: Принимаете ли вы какие-либо лекарства для сердца?",
    "Вопрос 4: Были ли у вас ранее сердечные приступы?",
    "Вопрос 5: Как вы оцениваете свой уровень стресса?",
    "Вопрос 6: Ваш возраст?",
    "Вопрос 7: Ваш пол?"
]
@router.message(lambda message: message.text == "Анкета")
async def start_questionnaire_handler(message: types.Message):
    await message.answer("Нажмите кнопку для начала анкетирования.", reply_markup=get_questionnaire_keyboard())

@router.callback_query(lambda callback: callback.data == "start_questionnaire")
async def process_start_questionnaire(callback: types.CallbackQuery, state: FSMContext):
      await callback.message.answer(questions[0])
      await update_user_questionnaire_step(callback.from_user.id, QuestionnaireState.QUESTION_1)
      await state.update_data(questionnaire_answers={})
      await callback.answer()

@router.message(QuestionnaireState.QUESTION_1)
async def process_question_1(message: types.Message, state: FSMContext):
     await state.update_data(questionnaire_answers={'question_1': message.text})
     await message.answer(questions[1])
     await update_user_questionnaire_step(message.from_user.id, QuestionnaireState.QUESTION_2)

@router.message(QuestionnaireState.QUESTION_2)
async def process_question_2(message: types.Message, state: FSMContext):
     data = await state.get_data()
     answers = data['questionnaire_answers']
     answers.update({'question_2': message.text})
     await state.update_data(questionnaire_answers=answers)
     await message.answer(questions[2])
     await update_user_questionnaire_step(message.from_user.id, QuestionnaireState.QUESTION_3)

@router.message(QuestionnaireState.QUESTION_3)
async def process_question_3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answers = data['questionnaire_answers']
    answers.update({'question_3': message.text})
    await state.update_data(questionnaire_answers=answers)
    await message.answer(questions[3])
    await update_user_questionnaire_step(message.from_user.id, QuestionnaireState.QUESTION_4)

@router.message(QuestionnaireState.QUESTION_4)
async def process_question_4(message: types.Message, state: FSMContext):
     data = await state.get_data()
     answers = data['questionnaire_answers']
     answers.update({'question_4': message.text})
     await state.update_data(questionnaire_answers=answers)
     await message.answer(questions[4])
     await update_user_questionnaire_step(message.from_user.id, QuestionnaireState.QUESTION_5)

@router.message(QuestionnaireState.QUESTION_5)
async def process_question_5(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answers = data['questionnaire_answers']
    answers.update({'question_5': message.text})
    await state.update_data(questionnaire_answers=answers)
    await message.answer(questions[5])
    await update_user_questionnaire_step(message.from_user.id, QuestionnaireState.QUESTION_6)

@router.message(QuestionnaireState.QUESTION_6)
async def process_question_6(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answers = data['questionnaire_answers']
    answers.update({'question_6': message.text})
    await state.update_data(questionnaire_answers=answers)
    await message.answer(questions[6])
    await update_user_questionnaire_step(message.from_user.id, QuestionnaireState.QUESTION_7)

@router.message(QuestionnaireState.QUESTION_7)
async def process_question_7(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answers = data['questionnaire_answers']
    answers.update({'question_7': message.text})
    await state.update_data(questionnaire_answers=answers)
    user_id = message.from_user.id
    update_user(user_id, {'questionnaire_answers': json.dumps(answers)})
    await message.answer("Спасибо за ответы! Анкетирование завершено.", reply_markup=get_main_keyboard())
    await state.clear()
    await update_user_questionnaire_step(user_id, None)