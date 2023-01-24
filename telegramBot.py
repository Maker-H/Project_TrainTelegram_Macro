import telegram 
import asyncio
from pprint import pprint

async def main():
    my_token = ''
    chat_id = 
    speak = "this is bot"

    bot = telegram.Bot(token = my_token)
    updates = await bot.getUpdates()
    await bot.sendMessage(chat_id = chat_id, text=speak)
    for u in updates:
        pprint(u.message)
asyncio.run(main())