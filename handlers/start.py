from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Привет! Отправь мне фото с подписью, и я сделаю из него мем.\n\n"
        "Формат подписи:\n"
        "*Верхний текст / Нижний текст*\n\n"
        "или через перенос строки\n"
        "*Верхний текст\nНижний текст*\n\n",
        parse_mode=ParseMode.MARKDOWN
    )