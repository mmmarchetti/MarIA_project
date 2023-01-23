from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import logging
import openai
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)


def image_generation(text):
    """Generate an answer image based in the text"""
    response = openai.Image.create(
        prompt=text,
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']


def text_generation(text):
    """Generate an answer text based in the text"""
    model_engine = "text-davinci-003"

    completions = openai.Completion.create(engine=model_engine,
                                           prompt=text,
                                           max_tokens=1024,
                                           n=1,
                                           stop=None,
                                           temperature=0.5)

    return completions.choices[0].text


async def response_generator(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Generate the response"""
    openai.api_key = OPENAI_API_KEY
    text = update.message.text

    create_images_word_list = ["imagem", "desenho", "desenhe", "figura",
                               "image", "figure", "drawing", "drawn"]

    if any(word in text for word in create_images_word_list):
        await update.message.reply_photo(image_generation(text))

    else:
        await update.message.reply_text(text_generation(text))


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await update.message.reply_text("Houve um erro em meu processamento, tente novamente")


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    try:
        # on different commands - answer in Telegram
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))

        # on non command i.e message - echo the message on Telegram
        # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, response_generator))
        # Run the bot until the user presses Ctrl-C
        application.run_polling()

    except Exception as e:
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, error))
        logging.info(e)


if __name__ == "__main__":
    main()
