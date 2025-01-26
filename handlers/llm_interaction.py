from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from utils.states import LLMInteractionState
from config import OPENAI_API_KEY
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from utils.prompts import Prompts
from utils.database import update_user_step

router = Router()
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
prompts = Prompts()

@router.message(lambda message: message.text == "Задать вопрос")
async def start_llm_handler(message: types.Message, state: FSMContext):
    await message.answer("Задайте свой вопрос:")
    await update_user_step(message.from_user.id, LLMInteractionState.ASK_LLM)


@router.message(LLMInteractionState.ASK_LLM)
async def process_llm_question(message: types.Message, state: FSMContext):
    question = message.text
    prompt = prompts.get_general_prompt()
    chain = LLMChain(llm=llm, prompt=prompt)
    response = await chain.arun(question=question)
    await message.answer(response)
    await state.clear()
    await update_user_step(message.from_user.id, None)