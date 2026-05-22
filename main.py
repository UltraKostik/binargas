# Telegram бот БинарГаз. Разработчик @UltraKostik

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.types import ErrorEvent

from config import get_bot_token, get_moderator_id

import file_handlers as fhd
import handlers as hd


def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("bot.log", encoding="utf-8"),
        ],
    )
    logging.getLogger("aiogram").setLevel(logging.WARNING)
    logging.getLogger("aiogram.dispatcher").setLevel(logging.WARNING)
    logging.getLogger("aiogram.event").setLevel(logging.WARNING)


logger = logging.getLogger(__name__)


async def main() -> None:
    setup_logging()
    logger.info("Запуск бота")

    try:
        bot_token = get_bot_token()
        moderator_id = get_moderator_id()
    except ValueError as e:
        logger.exception(f"Критическая ошибка при инициализации переменных окружения: {e}")
        return

    bot: Bot = Bot(token=bot_token)
    dp: Dispatcher = Dispatcher()

    dp.include_router(hd.router)
    dp.include_router(fhd.router)

    @dp.errors()
    async def handle_errors(event: ErrorEvent) -> bool:
        logger.exception(f"Ошибка в обработчике: {event.exception}")

        if event.update.callback_query:
            await event.update.callback_query.answer("❌ Ошибка. Попробуйте позже.")
        elif event.update.message:
            await event.update.message.answer("❌ Ошибка. Попробуйте позже.")

        return True

    logger.info("Бот успешно инициализирован!")
    logger.info("Запуск polling...")

    try:
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
