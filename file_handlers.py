#Telegram бот БинарГаз. Разработчик @UltraKostik

from aiogram import F, Router
from aiogram.types import CallbackQuery, FSInputFile
from time import ctime
import keyboards as kb
import logging
logger = logging.getLogger(__name__)
router = Router()
@router.callback_query(F.data == "model_3х")
async def model3x_handler(callback: CallbackQuery):
    try:
        document = FSInputFile(
            path="files/РЭ_Бинар_ХХ_ХХХ_Х_актуально_на_25_08_2025_коэффициенты_ИК_и_ТК,.docx",
            filename="РЭ_Бинар_3x_актуально_2025.docx"
        )
        await callback.message.answer_document(
            document=document,
            caption="📖 Руководство по эксплуатации Бинар 3x\n\n"
                   "📄 Формат: DOCX\n"
                   "📏 Страниц: 62\n",
            reply_markup=kb.back_keyboard
        )
        await callback.answer()
    except Exception as e:
        await callback.answer(f"⚠️ Произошла ошибка. Пожалуйста, попробуйте позже.")
        logger.error(f"[{ctime()}]. Ошибка в model3x_handler: {type(e).__name__}: {e}")  
@router.callback_query(F.data == "model_6х")
async def model6х_handler(callback: CallbackQuery):
    try:
        document = FSInputFile(
            path="files/РЭ Бинар-ХХ-ХХХ-Х-Х (Б,Н).docx",
            filename="РЭ Бинар-ХХ-ХХХ-Х-Х (Б,Н).docx"
        )
        await callback.message.answer_document(
            document=document,
            caption="📖 Руководство по эксплуатации Бинар 6x\n\n"
                   "📄 Формат: DOCX\n"
                   "📏 Страниц: 96\n",
            reply_markup=kb.back_keyboard
        )
        await callback.answer()
    except Exception as e:
        await callback.answer(f"⚠️ Произошла ошибка. Пожалуйста, попробуйте позже.")
        logger.error(f"[{ctime()}]. Ошибка в model6х_handler: {type(e).__name__}: {e}")      
@router.callback_query(F.data == "model_7х")
async def model7х_handler(callback: CallbackQuery):
    try:
        document = FSInputFile(
            path="files/РЭ_Бинар_ХХ_ХХХ_Х_новый_РЕЛЕ_УХЛ_1.docx",
            filename="РЭ_Бинар_7x_новый_РЕЛЕ_УХЛ.docx"
        )
        await callback.message.answer_document(
            document=document,
            caption="📖 Руководство по эксплуатации Бинар 7x\n\n"
                   "📄 Формат: DOCX\n"
                   "📏 Страниц: 38\n",
            reply_markup=kb.back_keyboard
        )
        await callback.answer()
    except Exception as e:
        await callback.answer(f"⚠️ Произошла ошибка. Пожалуйста, попробуйте позже.")
        logger.error(f"[{ctime()}]. Ошибка в model7х_handler: {type(e).__name__}: {e}")
@router.callback_query(F.data == "model_1П")
async def model1p_handler(callback: CallbackQuery):
    try:
        document = FSInputFile(
            path= "files/РЭ_Бинар_1П_Брошюра_новый_02092024_методы_измерения+зонд_новая_клавиатура.docx",
            filename="РЭ_Бинар_1П_Брошюра_новый_02092024_методы_измерения_зонд_новая_клавиатура.docx"
        )
        await callback.message.answer_document(
            document=document,
            caption="📖 Руководство по эксплуатации Бинар 1П\n\n"
                   "📄 Формат: DOCX\n"
                   "📏 Страниц: 15\n",
            reply_markup=kb.back_keyboard
        )
        await callback.answer()
    except Exception as e:
        await callback.answer(f"⚠️ Произошла ошибка. Пожалуйста, попробуйте позже.")
        logger.error(f"[{ctime()}]. Ошибка в model1p_handler: {type(e).__name__}: {e}")
@router.callback_query(F.data == "model_XXДХ")
async def modelxxdh_handler(callback: CallbackQuery):
    try:
        document = FSInputFile(
            path="files/РЭ БСИ Бинар_АГ_20220127.pdf",
            filename="РЭ_БСИ_Бинар_XXДХ_вертикальный.pdf"
        )
        await callback.message.answer_document(
            document=document,
            caption="📖 Руководство по эксплуатации Бинар XXДХ (Вертикальный)\n\n"
                   "📄 Формат: PDF\n"
                   "📏 Страниц: 22\n",
            reply_markup=kb.back_keyboard
        )
        await callback.answer()
    except Exception as e:
        await callback.answer(f"⚠️ Произошла ошибка. Пожалуйста, попробуйте позже.")
        logger.error(f"[{ctime()}]. Ошибка в modelxxdh_handler: {type(e).__name__}: {e}")
@router.callback_query(F.data == "model_1хХДХ")
async def model1xxdh_handler(callback: CallbackQuery):
    try:
        document = FSInputFile(
            path="files/Бинар 1хХХХ РЭ.docx",
            filename="РЭ_Бинар_1xХДХ_одноканальный.docx"
        )
        await callback.message.answer_document(
            document=document,
            caption="📖 Руководство по эксплуатации Бинар 1хХДХ\n\n"
                   "📄 Формат: DOCX\n"
                   "📏 Страниц: 45\n",
            reply_markup=kb.back_keyboard
        )
        await callback.answer()
    except Exception as e:
        await callback.answer(f"⚠️ Произошла ошибка. Пожалуйста, попробуйте позже.")
        logger.error(f"[{ctime()}]. Ошибка в model1xxdh_handler: {type(e).__name__}: {e}")
@router.callback_query(F.data == "model_XXПХ")
async def modelxxph_handler(callback: CallbackQuery):
    try:
        document = FSInputFile(
            path="files/РЭ БСИ Бинар_исп. 02_им. Забабахина.doc",
            filename="РЭ_БСИ_Бинар_XXПХ_горизонтальный.doc"
        )
        await callback.message.answer_document(
            document=document,
            caption="📖 Руководство по эксплуатации Бинар XXПХ (Горизонтальный)\n\n"
                   "📄 Формат: DOC\n"
                   "📏 Страниц: 21\n",
            reply_markup=kb.back_keyboard
        )
        await callback.answer()
    except Exception as e:
        await callback.answer(f"⚠️ Произошла ошибка. Пожалуйста, попробуйте позже.")
        logger.error(f"[{ctime()}]. Ошибка в modelxxph_handler: {type(e).__name__}: {e}")
@router.callback_query(F.data == "present")
async def present_handler(callback: CallbackQuery):
    try:
        document = FSInputFile(
            path= "files/АСКПВ на базе анализаторов Protea.pdf",
            filename="ASKPV_Protea_System.pdf"
        )
        await callback.message.answer_document(
            document=document,
            caption="📖 АСКПВ на базе анализаторов Protea\n\n"
                   "📄 Формат: PDF\n"
                   "📏 Страниц: 60\n",
            reply_markup=kb.back_keyboard
        )
        await callback.answer()
    except Exception as e:
        await callback.answer(f"⚠️ Произошла ошибка. Пожалуйста, попробуйте позже.")
        logger.error(f"[{ctime()}]. Ошибка в present_handler: {type(e).__name__}: {e}")  
@router.callback_query(F.data == "certificates")
async def certificates_handler(callback: CallbackQuery):
    try:
        document = FSInputFile(
            path= "files/2022-85948-22.pdf",
            filename="Описание типа средства измерений.pdf"
        )
        await callback.message.answer_document(
            document=document,
            caption="📖 Описание типа средства измерений\n\n"
                   "📄 Формат: PDF\n"
                   "📏 Страниц: 47\n",
            reply_markup=kb.back_keyboard
        )
        await callback.answer()
    except Exception as e:
        await callback.answer(f"⚠️ Произошла ошибка. Пожалуйста, попробуйте позже.")
        logger.error(f"[{ctime()}]. Ошибка в certificates_handler: {type(e).__name__}: {e}")