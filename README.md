# MemegramBot

A simple Telegram bot that turns any photo with a caption into a classic meme using the Impact font right in the chat.

## Features

- `/start` command with a quick usage guide
- Flexible caption parsing: `TOP / BOTTOM`, `TOP\nBOTTOM`, or bottom-only text
- Automatic square crop, font auto-sizing, and text wrapping to fit the image
- White text with black stroke, rendered in the classic Impact font
- JPEG compression before sending the result back to Telegram

## Tech stack

- Python 3.14
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - Telegram Bot API framework
- [Pillow](https://python-pillow.org/) - image processing
- [uv](https://docs.astral.sh/uv/) - dependency management
- python-dotenv - environment configuration

## Getting started

1. Install dependencies:
  ```bash
  uv sync
  ```
  
2. Add the font file:
  Place impact.ttf (or any TTF font of your choice) into the assets/fonts/ directory.

3. Create a `.env` file in the project root with your bot token:
  ```
  TELEGRAM_BOT_TOKEN=your_token_here
  ```

4. Run the bot:
  ```bash
  uv run main.py
  ```

## Usage

Send the bot a photo with a caption:

```
Top text / Bottom text
```

or split across two lines:

```
Top text
Bottom text
```

A caption with no separator is used as bottom text only.
