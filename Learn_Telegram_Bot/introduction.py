import asyncio
import telegram
import pwd_token
async def main():
    bot = telegram.Bot(pwd_token.get_token())
    async with bot:
        # print(await bot.get_me())
        # async with bot: ensures that PTB can properly acquire and release resources.
        
        print((await bot.get_updates())[0])
        # if i send text this method fetch the update

        await bot.send_message(text='Hi SOM!', chat_id=pwd_token.get_chatid())
        


if __name__ == '__main__':
    asyncio.run(main())