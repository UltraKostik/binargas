# BinargasBot

Telegram-бот для компании «БИНАР»: руководства по эксплуатации, сертификаты и обратная связь с менеджером.

## Функционал

- 📖 Руководства по эксплуатации: отправка файлов (DOCX, DOC, PDF) для различных моделей газоанализаторов
- 📄 Сертификаты: отправка официальных документов и лицензий
- 👨‍💼 Связь с менеджером: форма обратной связи с уведомлением модератора

## Технологии

- Python 3.14+
- aiogram 3.x
- FSM (Finite State Machine)
- python-dotenv

## Установка и запуск

**1. Клонировать репозиторий**

```bash
git clone https://github.com/UltraKostik/BinargasBot.git
cd BinargasBot
```

**2. Создать виртуальное окружение**
```bash
python -m venv venv
```

**3. Активировать окружение**
```bash
source venv/bin/activate # Linux/macOS
```
```bash
venv\Scripts\activate # Windows
```

**4. Установить зависимости**
```bash
pip install -r requirements.txt
```

**5. Настроить переменные окружения**
```bash
cp .env.example .env
```
Отредактировать .env, указать BOT_TOKEN и MODERATOR_ID

**6. Запустить бота**
```bash
python main.py
```


## Разработчик

- Telegram: [@UltraKostik](https://t.me/UltraKostik)
- GitHub: [UltraKostik](https://github.com/UltraKostik)
- DTF: [ladvd](https://dtf.ru/ladvd)

## Лицензия

Проект разработан для компании «БИНАР». Все права защищены.
