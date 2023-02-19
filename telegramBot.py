import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
import pwd_token
import korail

# log when thigs don't work as expected
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# porcess a specific type of update
# update keyword is which contains all the information and data that are coming from telegram(like msg)
# context is which contains information and data about the status of library itself (like Bot, Application object)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=tmp_answer)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # update.message.text brings what i enter in telegram
    
    global tmp_answer    
    if update.message.text == 'global':
        await context.bot.send_message(chat_id=update.effective_chat.id, text=tmp_answer)
    # await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="starting caps")
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
    


if __name__ == '__main__':
    # create an Application object
    application = ApplicationBuilder().token(pwd_token.get_token()).build()
    # tell bot listen to /start commands
    start_handler = CommandHandler('start', start)
    # echoing bot
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    caps_handler = CommandHandler('caps', caps)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)

    # runs bot until i hit ctrl+c
    application.run_polling()