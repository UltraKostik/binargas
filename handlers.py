#Telegram бот БинарГаз. Разработчик @UltraKostik

import os, re, logging
from time import ctime
from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
from aiogram.exceptions import MessageNotModified
import keyboards as kb
from dotenv import load_dotenv
logger = logging.getLogger(__name__)
load_dotenv()
MODERATOR_ID = int(os.getenv("MODERATOR_ID"))
router = Router()
class UserStates(StatesGroup):
    contact_name = State()
    contact_info = State() 
class Moderator(StatesGroup):
    wait = State()  
@router.callback_query(F.data == "back_main")
@router.message(F.text == "/start")
async def start_handler(update: Message | CallbackQuery):
        welcome_text = (
            "Добро пожаловать в официальный бот компании «БИНАР»! 🛡️\n\n"
            "Мы производим российские газоанализаторы для контроля горючих газов "
            "и паров с полным циклом поддержки на территории РФ.\n\n"
            "<b>Какая информация вас интересует? ⬇️</b>"
        )
        if isinstance(update, CallbackQuery):
            await update.message.answer(welcome_text, reply_markup=kb.main_keyboard, parse_mode="HTML")
            await update.answer()
        else:
            await update.answer(welcome_text, reply_markup=kb.main_keyboard, parse_mode="HTML")   
@router.callback_query(F.data == "manual")
async def manual_handler(callback: CallbackQuery):
    try:
        await callback.message.edit_text(
            "⚙️ Модели Бинар\n\n"
            "Какой Бинар вас интересует?",
            reply_markup=kb.models_keyboard
        )
        await callback.answer()
    except MessageNotModified:
        await callback.answer()
    except Exception as e:
        await callback.answer(f"⚠️ Произошла ошибка. Пожалуйста, попробуйте позже.")
        logger.error(f"[{ctime()}]. Ошибка в manual_handler: {type(e).__name__}: {e}")
@router.callback_query(F.data == "contact")
async def contact_handler(callback: CallbackQuery, state: FSMContext):
    try:
        await state.set_state(UserStates.contact_name)
        await callback.message.edit_text(
            "👨‍💼 Связь с менеджером\n\n"
            "Пожалуйста, напишите как можно к вам обращаться:\n"
            "Например: <i>Иванов Иван</i> или <i>Иван</i>",
            reply_markup=kb.back_keyboard,
            parse_mode="HTML"
        )
        await callback.answer()
    except MessageNotModified:
        await callback.answer()
    except Exception as e:
        await callback.answer(f"⚠️ Произошла ошибка. Пожалуйста, попробуйте позже.")
        logger.error(f"[{ctime()}]. Ошибка в contact_handler: {type(e).__name__}: {e}")      
@router.message(F.text, UserStates.contact_name)
async def get_name_handler(message: Message, state: FSMContext):
        name = message.text.strip()
        if not name:
            await message.answer("❌ Пожалуйста, введите ваше имя.")
            return
        if name.isdigit():
            await message.answer(
                "❌ Имя не должно состоять только из цифр.\n"
                "Введите настоящее имя, например: <i>Иван</i> или <i>Иванов Иван</i>",
                parse_mode="HTML"
            )
            return
        await state.update_data(name=name)
        await state.set_state(UserStates.contact_info)
        await message.answer(
        f"💬 Напишите ваш вопрос или сообщение:\n\n"
        f"<i>Опишите что вас интересует, задайте вопрос или оставьте комментарий</i>",
        parse_mode="HTML"
        )
@router.message(F.text, UserStates.contact_info)
async def get_info_handler(message: Message, state: FSMContext):
    try:
        info = message.text
        if not info:
            await message.answer("❌ Пожалуйста, введите ваш вопрос или сообщение.")
            return
        name = (await state.get_data()).get('name', 'Не указано')
        await message.answer(
            f"✅ Заявка принята! \n\n"
            f"📋 Ваши данные:\n"
            f"• Имя: {name}\n"
            f"• Сообщение: {info}\n\n"
            f"📞 Менеджер свяжется с вами в ближайшее время.\n\n",
            parse_mode="HTML",
            reply_markup=kb.back_keyboard
        )
        user = message.from_user
        await message.bot.send_message(
            chat_id = MODERATOR_ID,
            text=
            f"📨 <b>НОВАЯ ЗАЯВКА ОТ {'@' + user.username if user.username else f'<a href=\"tg://user?id={user.id}\">Пользователь</a>'}</b>\n\n"
            f"• ID: <code>{user.id}</code>\n"
            f"• Контактное имя: {name}\n"
            f"• Имя из профиля Telegram: {user.full_name or 'Не указано'}\n"
            f"• Сообщение: {info}\n\n"
            f"🕒 <i>{ctime()}</i>", 
            parse_mode="HTML",
            reply_markup=kb.moderator_keyboard
        )
        logger.info(f"[{ctime()}] Заявка отправлена модератору ID: {MODERATOR_ID}")
    except Exception as e:
        await message.answer(f"⚠️ Не удалось отправить заявку модератору. Пожалуйста, попробуйте позже.")
        logger.error(f"[{ctime()}]. Ошибка в get_info_handler: {type(e).__name__}: {e}")
    finally:
        await state.clear()
@router.callback_query(F.data == "send_message_moderator")
async def send_message_handler(callback: CallbackQuery, state: FSMContext):
        message_text = callback.message.text
        match = re.search(r'• ID:\s*(\d+)', message_text)
        if match:
            user_id = int(match.group(1))
            await state.update_data(reply_user_id=user_id)
            await state.set_state(Moderator.wait)
            await callback.message.answer(
                f"💬 Напишите ответ для пользователя (ID: {user_id}):"
            )
        else:
            await callback.answer("❌ Не найден ID пользователя в сообщении")
            return
@router.message(Moderator.wait)
async def moderator_reply_handler(message: Message, state: FSMContext):
    try:
        if message.chat.id != MODERATOR_ID:
            return
        data = await state.get_data()
        user_id = data.get("reply_user_id")
        if not user_id:
            await message.answer("❌ Ошибка: не найден ID пользователя")
            return
        await message.bot.send_message(
            chat_id=user_id,
            text=f"📩 <b>Ответ от менеджера компании «БИНАР»</b>\n\n{message.text}\n\n🛡️ С уважением, команда «БИНАР»",
            parse_mode="HTML"
        )
        await message.answer(f"✅ Ответ отправлен пользователю ID: {user_id}")
    except Exception as e:
        await message.answer(f"⚠️ Не удалось отправить ответ пользователю. Возможно, он заблокировал бота. Пожалуйста, попробуйте позже.")
        logger.error(f"[{ctime()}]. Ошибка в moderator_reply_handler: {type(e).__name__}: {e}")
    finally:
        await state.clear()