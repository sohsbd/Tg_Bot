from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_keyboard():
    """Возвращает основную клавиатуру."""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Информация о заболеваниях")],
            [KeyboardButton(text="Рекомендации")],
            [KeyboardButton(text="Задать вопрос"),
             KeyboardButton(text="Анкета")],
            [KeyboardButton(text="Отзыв")]
        ],
        resize_keyboard=True
    )
    return keyboard