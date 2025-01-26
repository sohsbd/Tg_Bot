from aiogram.fsm.state import StatesGroup, State

class RegistrationState(StatesGroup):
    GET_NAME = State()
    GET_LAST_NAME = State()

class QuestionnaireState(StatesGroup):
    QUESTION_1 = State()
    QUESTION_2 = State()
    QUESTION_3 = State()
    QUESTION_4 = State()
    QUESTION_5 = State()
    QUESTION_6 = State()
    QUESTION_7 = State()

class LLMInteractionState(StatesGroup):
    ASK_LLM = State()

class FeedbackState(StatesGroup):
    FEEDBACK = State()