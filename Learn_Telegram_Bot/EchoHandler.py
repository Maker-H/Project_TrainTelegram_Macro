import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
import telegram

tmp_answer = 0

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
    pass
    # context.args = receive the arguments as a list
    # await context.bot.send_message(chat_id=update.effective_chat.id, text="starting caps")
    # global tmp_answer
    # update.message.text
    # tmp_answer = update.message.text
    # await context.bot.send_message(chat_id=update.effective_chat.id, text='stored')

if __name__ == '__main__':
    # create an Application object
    application = ApplicationBuilder().token('5856045997:AAGMrDNilRAlRNWeI-VzLg7_uWsqbD6t9BA').build()
    # tell bot listen to /start commands
    start_handler = CommandHandler('start', start)
    # eching bot
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    caps_handler = CommandHandler('caps', caps)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)

    # runs bot until i hit ctrl+c
    application.run_polling()