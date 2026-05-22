#Telegram бот БинарГаз. Разработчик @UltraKostik

import logging
from time import ctime

from aiogram import F, Router
from aiogram.types import CallbackQuery, FSInputFile

import config
import keyboards as kb

logger = logging.getLogger(__name__)
router = Router()


def file_handler_factory(callback_data: str, path: str, filename: str, caption: str):
    async def handler(callback: CallbackQuery) -> None:
        try:
            document = FSInputFile(path=path, filename=filename)
            await callback.message.answer_document(
                document=document,
                caption=caption,
                reply_markup=kb.back_keyboard
            )
            await callback.answer()
        except FileNotFoundError as e:
            await callback.answer(f"⚠️ Файл временно недоступен. Пожалуйста, попробуйте позже, либо обратитесь к менеджеру.")
            logger.error(f"[{ctime()}]. Хендлер {callback_data}. Ошибка: {type(e).__name__}: {e}")  
        except Exception as e:
            await callback.answer(f"⚠️ Произошла ошибка. Пожалуйста, попробуйте позже, либо обратитесь к менеджеру.")
            logger.error(f"[{ctime()}]. Хендлер {callback_data}. Ошибка: {type(e).__name__}: {e}")
    return handler

for callback_data, file_info in config.FILES_CONFIG.items():
    handler = file_handler_factory(
        callback_data=callback_data,
        path=file_info["path"],
        filename=file_info["filename"],
        caption=file_info["caption"]
    )
    router.callback_query(F.data == callback_data)(handler)