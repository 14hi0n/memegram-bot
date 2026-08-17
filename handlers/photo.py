import asyncio
import io

from PIL import Image
from telegram import Update
from telegram.ext import ContextTypes

from services.meme_renderer import compress_for_telegram, render_meme_text


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    It edits photos and generates memes with text.
    """
    if not update.message or not update.message.photo or not update.message.caption:
        return

    # get the photo with the highest resolution
    photo_file = await update.message.photo[-1].get_file()

    # downloads the file to the buffer
    photo_bytes = await photo_file.download_as_bytearray()
    input_image = Image.open(io.BytesIO(photo_bytes))

    # parse the signature
    caption = update.message.caption or ""

    if "/" in caption:
        parts = caption.split("/", 1)
        top_text, bottom_text = parts[0].strip(), parts[1].strip()

    elif "\n" in caption:
        parts = caption.split("\n", 1)
        top_text, bottom_text = parts[0].strip(), parts[1].strip()

    else:
        top_text = None
        bottom_text = caption.strip()

    # generates a meme
    meme_bytes = await asyncio.to_thread(_process_meme, input_image, top_text, bottom_text)

    # sends the meme back
    await update.message.reply_photo(photo=io.BytesIO(meme_bytes), caption="Вот мем!")


def _process_meme(image: Image.Image, top_text: str | None, bottom_text: str) -> bytes:
    """
    Processes the image and generates a meme with the given text.
    """
    rendered = render_meme_text(image, top_text, bottom_text)
    return compress_for_telegram(rendered)