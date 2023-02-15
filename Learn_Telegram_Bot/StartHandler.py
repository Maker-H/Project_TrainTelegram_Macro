import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import pwd_token

# log when thigs don't work as expected
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# porcess a specific type of update
# update keyword is which contains all the information and data that are coming from telegram(like msg)
# context is which contains information and data about the status of library itself (like Bot, Application object)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
        user_text = update.message.text



if __name__ == '__main__':
    # create an Application object
    application = ApplicationBuilder().token(pwd_token.get_token()).build()
    
    # tell bot listen to /start commands
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    # runs bot until i hit ctrl+c
    application.run_polling()