#Telegram бот БинарГаз. Разработчик @UltraKostik

from aiogram import F, Router
from aiogram.types import CallbackQuery, FSInputFile
from time import ctime
import keyboards as kb
import logging, config
logger = logging.getLogger(__name__)
router = Router()

def file_handler_factory(path: str, filename: str, caption: str):
    async def handler(callback: CallbackQuery):
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
            logger.error(f"[{ctime()}]. Функция {callback_data}. Ошибка: {type(e).__name__}: {e}")  
        except Exception as e:
            await callback.answer(f"⚠️ Произошла ошибка. Пожалуйста, попробуйте позже, либо обратитесь к менеджеру.")
            logger.error(f"[{ctime()}]. Функция {callback_data}. Ошибка: {type(e).__name__}: {e}")
    return handler

for callback_data, file_info in config.FILES_CONFIG.items():
    handler = file_handler_factory(
        path=file_info["path"],
        filename=file_info["filename"],
        caption=file_info["caption"]
    )
    router.callback_query(F.data == callback_data)(handler)