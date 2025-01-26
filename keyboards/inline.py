from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_feedback_keyboard():
    """Возвращает клавиатуру с кнопкой для отзыва."""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Оставить отзыв", callback_data="feedback")]
    ])
    return keyboard


def get_questionnaire_keyboard():
    """Возвращает клавиатуру с кнопкой для начала анкетирования."""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Начать анкетирование", callback_data="start_questionnaire")]
    ])
    return keyboard