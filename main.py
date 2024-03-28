
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv
import logging
load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG

)
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Здоров {update.effective_user.first_name}')
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    massage = update.message.text.lower()
    if 'привіт' in massage:
        reply_text = f"Доброго дня {update.effective_user.first_name}"
    else:
        reply_text = 'Я тебе не зрозумів.'


    await update.message.reply_text(reply_text)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Start {update.effective_user.first_name}')
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("Hello", hello))
app.add_handler(CommandHandler("Start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))


app.run_polling()