# Telegram бот БинарГаз. Разработчик @UltraKostik

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📖 Руководство по эксплуатации", callback_data="manual")],
        [InlineKeyboardButton(text="📄 Сертификаты", callback_data="certificates")],
        [InlineKeyboardButton(text="📊 Презентационные материалы", callback_data="present")],
        [InlineKeyboardButton(text="👨‍💼 Связаться с менеджером", callback_data="contact")],
    ]
)

models_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="3х", callback_data="model_3х"),
            InlineKeyboardButton(text="6х", callback_data="model_6х"),
            InlineKeyboardButton(text="7х", callback_data="model_7х"),
        ],
        [
            InlineKeyboardButton(text="1П", callback_data="model_1П"),
            InlineKeyboardButton(text="XXДХ", callback_data="model_XXДХ"),
            InlineKeyboardButton(text="1хХДХ", callback_data="model_1хХДХ"),
        ],
        [
            InlineKeyboardButton(text="XXПХ", callback_data="model_XXПХ"),
            InlineKeyboardButton(text="🔙 Назад", callback_data="back_main"),
        ],
    ]
)

moderator_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="✉️ Ответить на заявку", callback_data="send_message_moderator")],
    ]
)

back_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_main")],
    ]
)