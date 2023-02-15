# https://jow1025.tistory.com/317
import telegram 
import asyncio
from pprint import pprint
import pwd_token

async def main():
    my_token = pwd_token.get_token()
    chat_id = pwd_token.get_chatid()
    speak = "this is bot"

    bot = telegram.Bot(token = my_token)
    updates = await bot.getUpdates()
    await bot.sendMessage(chat_id = chat_id, text=speak)
    for u in updates:
        pprint(u.message)
asyncio.run(main())

