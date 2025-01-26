from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message, CallbackQuery
from utils.database import add_user, update_user
import datetime

class UserLogMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
         Dict[str, Any],
    ) -> Any:

        if isinstance(event, Message):
            user_id = event.from_user.id
            username = event.from_user.username
            first_name = event.from_user.first_name
            last_name = event.from_user.last_name
            message_text = event.text
            log_data = {
                'user_id': user_id,
                'username': username,
                'first_name': first_name,
                'last_name': last_name,
                'message': message_text,
                'timestamp': str(datetime.datetime.now())
             }
        elif isinstance(event, CallbackQuery):
            user_id = event.from_user.id
            username = event.from_user.username
            first_name = event.from_user.first_name
            last_name = event.from_user.last_name
            callback_data = event.data
            log_data = {
                'user_id': user_id,
                'username': username,
                'first_name': first_name,
                'last_name': last_name,
                'callback_data': callback_data,
                'timestamp': str(datetime.datetime.now())
             }
        else:
            return await handler(event, data)


        # Логирование действий в консоль
        print(f"User event: {log_data}")

        # Сохраняем действия пользователя в БД (в нашем случае CSV)
        try:
            add_user(user_id, username, first_name, last_name)
        except:
            pass
        return await handler(event, data)
