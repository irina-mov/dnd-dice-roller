import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()  # читает .env при локальном запуске (на Railway .env не нужен — там переменные в настройках)

WEB_APP_URL = "https://irina-mov.github.io/dnd-dice-roller/"
BOT_TOKEN   = os.environ["BOT_TOKEN"]


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
    import asyncio
    asyncio.set_event_loop(asyncio.new_event_loop())  # fix для Python 3.12+
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    app.run_polling()
