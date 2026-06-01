import os
import asyncio
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

WEB_APP_URL = "https://irina-mov.github.io/dnd-dice-roller/"


async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    button = InlineKeyboardButton(
        text="🎲 Бросить кубик!",
        web_app=WebAppInfo(url=WEB_APP_URL),
    )
    await update.message.reply_text(
        "Добро пожаловать! Нажми кнопку чтобы открыть кубики D&D 🐉",
        reply_markup=InlineKeyboardMarkup([[button]]),
    )


if __name__ == "__main__":
    load_dotenv()  # читает .env при локальном запуске

    # debug: показать все ключи окружения
    print("ENV KEYS:", sorted(os.environ.keys()))

    token = os.environ.get("BOT_TOKEN")
    print("BOT_TOKEN found:", bool(token), "| length:", len(token) if token else 0)
    if not token:
        raise SystemExit("Ошибка: переменная BOT_TOKEN не задана!")

    asyncio.set_event_loop(asyncio.new_event_loop())
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    app.run_polling()
