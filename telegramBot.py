import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
import pwd_token
import korail

cmd = '/pwd 텔레그램_챗봇_시작_비밀번호 \n ex) /pwd 1234 \n' \
+ '/id 코레일_아이디 비밀번호 \n /id 139123 1234qqe \n' \
+ '/d 년/월/일 \'/\'를 꼭 삽입하여야 합니다. (/d 만 입력하시면 오늘 날짜로 설정됩니다)\n /d 23/12/31 \n' \
+ '/h 기차_시작_시간 (/h 만 입력하면 지금 시간으로 입력됩니다) \n /h 7 \n' \
+ '/s 기차_출발역 기차_도착역  \n /s 동대구 서울 \n' \
+ '/t 기차_타입1 or 기차_타입2 ex) ktx, 새마을, 무궁화 (/s 만 입력하시면 전체로 설정됩니다) \n /t ktx 새마을, /t ktx, /t \n' \
+ '/n 기차 개수 (상위 몇개의 기차를 예매하실지 선택해주세요. 2개를 선택하시면 입력하신 시간 기준 가까운 기차 2개 중 1개가 예매됩니다)\n /n 2 \n' \
+ '/list 는 기차목록을 보여주고 /start 를 입력하면 예매를 시작합니다'

cmd_simple = '/id(korail id pwd), /h(hour), /s(station1 station2), /t(train type), /n(number of reservation), /list, /start, /cmd, /simcmd'



# log when thigs don't work as expected
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# porcess a specific type of update
# update keyword is which contains all the information and data that are coming from telegram(like msg)
# context is which contains information and data about the status of library itself (like Bot, Application object)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='')

# Test
async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="starting caps")
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
    

# korail ID/PWD
async def korail_id_pwd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    korail.set_id(' '.join(context.args))
    await context.bot.send_message(chat_id=update.effective_chat.id, text='설정되었습니다')


# Setting train date
async def korail_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    korail.set_date(' '.join(context.args))
    await context.bot.send_message(chat_id=update.effective_chat.id, text='설정되었습니다')


# Setting departure hour
async def korail_hour(update: Update, context: ContextTypes.DEFAULT_TYPE):
    korail.set_hour(' '.join(context.args))
    await context.bot.send_message(chat_id=update.effective_chat.id, text='설정되었습니다')


# Setting station
async def korail_station(update: Update, context: ContextTypes.DEFAULT_TYPE):
    korail.set_station(' '.join(context.args))
    await context.bot.send_message(chat_id=update.effective_chat.id, text='설정되었습니다')


# Setting train type
async def korail_train_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    korail.set_train_type(' '.join(context.args))
    await context.bot.send_message(chat_id=update.effective_chat.id, text='설정되었습니다')


# Setting number of trains to reserve
async def korail_num_of_reservation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    korail.set_num_of_reservation(' '.join(context.args))
    await context.bot.send_message(chat_id=update.effective_chat.id, text='설정되었습니다')


# Show list of trains
async def korail_show_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    trains = korail.show_train_list()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=trains)


# Start reservation
async def korail_start_reservation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = korail.start_reservation()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=result)

# Show handler list
async def show_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='다시 명령어를 보고 싶으시면 /cmd 를, 간단히 명령어를 보고 싶다면 /simcmd 을 입력하세요')
    await context.bot.sendMessage(chat_id=update.effective_chat.id, text=cmd)

# Show simple handler list
async def show_simple_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='다시 명령어를 보고 싶으시면 /cmd 를, 간단히 명령어를 보고 싶다면 /simcmd 을 입력하세요')
    await context.bot.sendMessage(chat_id=update.effective_chat.id, text=cmd_simple)



if __name__ == '__main__':
    # create an Application object
    application = ApplicationBuilder().token(pwd_token.get_token()).build()


    # tell bot listen to /start commands
    caps_handler = CommandHandler('caps', caps)
    korail_id_pwd_handler = CommandHandler('id', korail_id_pwd)
    korail_date_handler = CommandHandler('d', korail_date)
    korail_hour_handler = CommandHandler('h', korail_hour)
    korail_station_handler = CommandHandler('s', korail_station)
    korail_train_type_handler = CommandHandler('t', korail_train_type)
    korail_num_of_reservation_handler = CommandHandler('n', korail_num_of_reservation)
    korail_show_list_handler = CommandHandler('list', korail_show_list)
    korail_start_reservation_handler = CommandHandler('start', korail_start_reservation)
    show_command_handler = CommandHandler('cmd', show_command)

    
    application.add_handler(caps_handler)
    application.add_handler(korail_id_pwd_handler)
    application.add_handler(korail_date_handler)
    application.add_handler(korail_hour_handler)
    application.add_handler(korail_station_handler)
    application.add_handler(korail_train_type_handler)
    application.add_handler(korail_num_of_reservation_handler)
    application.add_handler(korail_show_list_handler)
    application.add_handler(korail_start_reservation_handler)
    application.add_handler(show_command_handler)

    # runs bot until i hit ctrl+c
    application.run_polling()