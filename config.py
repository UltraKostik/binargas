#Telegram бот БинарГаз. Разработчик @UltraKostik

from pathlib import Path

BASE_DIR = Path(__file__).parent
FILES_DIR = BASE_DIR / "files"

FILES_CONFIG = {
    "model_3х": {
        "path": FILES_DIR / "РЭ_Бинар_3x.docx",
        "filename": "РЭ_Бинар_3x_актуально_2025.docx",
        "caption": "📖 Руководство по эксплуатации Бинар 3x\n\n📄 Формат: DOCX\n📏 Страниц: 62"
    },
    "model_6х": {
        "path": FILES_DIR / "РЭ_Бинар_6x.docx",
        "filename": "РЭ_Бинар_6x_актуально.docx",
        "caption": "📖 Руководство по эксплуатации Бинар 6x\n\n📄 Формат: DOCX\n📏 Страниц: 96"
    },
    "model_7х": {
        "path": FILES_DIR / "РЭ_Бинар_7x.docx",
        "filename": "РЭ_Бинар_7x_новый_РЕЛЕ.docx",
        "caption": "📖 Руководство по эксплуатации Бинар 7x\n\n📄 Формат: DOCX\n📏 Страниц: 38"
    },
    "model_1П": {
        "path": FILES_DIR / "РЭ_Бинар_1П.docx",
        "filename": "РЭ_Бинар_1П_брошюра.docx",
        "caption": "📖 Руководство по эксплуатации Бинар 1П\n\n📄 Формат: DOCX\n📏 Страниц: 15"
    },
    "model_XXДХ": {
        "path": FILES_DIR / "РЭ_Бинар_XXДХ.pdf",
        "filename": "РЭ_Бинар_XXДХ_вертикальный.pdf",
        "caption": "📖 Руководство по эксплуатации Бинар XXДХ (Вертикальный)\n\n📄 Формат: PDF\n📏 Страниц: 22"
    },
    "model_1хХДХ": {
        "path": FILES_DIR / "РЭ_Бинар_1хХДХ.docx",
        "filename": "РЭ_Бинар_1хХДХ_одноканальный.docx",
        "caption": "📖 Руководство по эксплуатации Бинар 1хХДХ\n\n📄 Формат: DOCX\n📏 Страниц: 45"
    },
    "model_XXПХ": {
        "path": FILES_DIR / "РЭ_Бинар_XXПХ.doc",
        "filename": "РЭ_Бинар_XXПХ_горизонтальный.doc",
        "caption": "📖 Руководство по эксплуатации Бинар XXПХ (Горизонтальный)\n\n📄 Формат: DOC\n📏 Страниц: 21"
    },
    "present": {
        "path": FILES_DIR / "АСКПВ_Protea.pdf",
        "filename": "ASKPV_Protea_System.pdf",
        "caption": "📖 АСКПВ на базе анализаторов Protea\n\n📄 Формат: PDF\n📏 Страниц: 60"
    },
    "certificates": {
        "path": FILES_DIR / "сертификат_2022.pdf",
        "filename": "Описание типа средства измерений.pdf",
        "caption": "📖 Описание типа средства измерений\n\n📄 Формат: PDF\n📏 Страниц: 47"
    }
}