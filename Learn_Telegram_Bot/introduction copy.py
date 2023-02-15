import asyncio
import logging
import telegram
from telegram.ext import Updater, MessageHandler, filters
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import pwd_token


token = pwd_token.get_token()
id = pwd_token.get_chatid()
queue = []
bot = telegram.Bot(token)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# updater
updater = Updater(bot=bot, update_queue=queue)
dispatcher = updater.dispatcher
#봇 
updater.start_polling()

def handler(update, context):
    user_text = update.message.text 
    if user_text == "ㅋㅋ": #ㅋㅋ라고 보내면 왜웃냐고 답장
        bot.send_message(chat_id=id, text="왜 웃냐") # 답장 보내기
    elif user_text == "웃겨서": 
        bot.send_message(chat_id=id, text="뭐가 웃긴데?") # 답장 보내기

echo_handler = MessageHandler(filters.text, handler)
dispatcher.add_handler(echo_handler)