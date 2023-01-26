from aiogram import Bot, Dispatcher
from aiogram.types import Message
import logging
import asyncio
from setting import settings
from aiogram.filters import CommandStart
from handlers.start import get_start
#from handlers.callback import get_pele, get_maradona


async def start():
    logging.basicConfig(level=logging.INFO,
                        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s')
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher()

    dp.message.register(get_start, CommandStart())
#    dp.message.register(get_queez)
#    dp.callback_query.register(get_pele)
#    dp.callback_query.register(get_maradona)




    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
