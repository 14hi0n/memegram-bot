from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import Config
from handlers.photo import handle_photo
from handlers.start import start


def main() -> None:
    application = ApplicationBuilder().token(Config.TELEGRAM_BOT_TOKEN).build()

    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    application.add_handler(CommandHandler("start", start))
    
    application.run_polling()


if __name__ == "__main__":
    main()
