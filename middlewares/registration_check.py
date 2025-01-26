from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message, CallbackQuery
from utils.database import get_user

class RegistrationCheckMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        Dict[str, Any],
    ) -> Any:
        if isinstance(event, Message):
            user_id = event.from_user.id
        elif isinstance(event, CallbackQuery):
            user_id = event.from_user.id
        else:
            return await handler(event, data)

        user = get_user(user_id)
        if user and user.get('registered', False):
            return await handler(event, data)
        else:
             if isinstance(event, Message):
                  await event.answer("Пожалуйста, сначала зарегистрируйтесь, использовав /start.")
             elif isinstance(event, CallbackQuery):
                  await event.answer("Пожалуйста, сначала зарегистрируйтесь, использовав /start.")
             return