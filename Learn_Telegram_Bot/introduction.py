import asyncio
import telegram

async def main():
    bot = telegram.Bot('')
    async with bot:
        # print(await bot.get_me())
        # async with bot: ensures that PTB can properly acquire and release resources.
        
        print((await bot.get_updates())[0])
        # if i send text this method fetch the update

        await bot.send_message(text='Hi SOM!', chat_id=)
        


if __name__ == '__main__':
    asyncio.run(main())