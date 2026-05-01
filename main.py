#Telegram бот БинарГаз. Разработчик @UltraKostik

import asyncio, logging, os, sys
from aiogram import Bot, Dispatcher
from aiogram.types import ErrorEvent
from dotenv import load_dotenv
import handlers as hd, file_handlers as fhd
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('bot.log', encoding='utf-8')
    ]
)
logging.getLogger("aiogram").setLevel(logging.WARNING)
logging.getLogger("aiogram.dispatcher").setLevel(logging.WARNING)
logging.getLogger("aiogram.event").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)
def load_config():
    load_dotenv()
    token = os.getenv('BOT_TOKEN')
    if not token:
        logger.error("BOT_TOKEN отсутствует в .env файле!")
        return None
    moderator_id = os.getenv('MODERATOR_ID')
    if not moderator_id:
        logger.error("MODERATOR_ID отсутствует в .env файле!")
        return None
    return token
async def main():
    logger.info("Запуск бота БинарГаз")
    token = load_config()
    if not token:
        logger.error("Не удалось загрузить конфигурацию. Бот остановлен.")
        return
    bot = None
    try:
        bot = Bot(token=token)
        dp = Dispatcher()
        dp.include_router(hd.router)
        dp.include_router(fhd.router)
        @dp.errors()
        async def handle_errors(event: ErrorEvent):
            logger.exception(f"Глобальная ошибка: {event.exception}")
            if event.update.callback_query:
                await event.update.callback_query.answer(
                    "❌ Произошла ошибка. Попробуйте позже."
                )
            elif event.update.message:
                await event.update.message.answer(
                    "❌ Произошла ошибка. Попробуйте позже."
                )
            return True
        logger.info("Бот успешно инициализирован")
        logger.info("Запуск polling...")
        await dp.start_polling(bot)
    except Exception as e:
        logger.exception(f"Ошибка во время работы бота: {e}")
    finally:
        if bot:
            await bot.session.close()
            logger.info("Сессия бота закрыта")
    logger.info("Бот завершил работу")
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен пользователем")
    except Exception as e:
        logger.exception(f"Критическая ошибка при запуске бота: {e}")