from aiogram.types import Message
from aiogram import Bot
from keyboards.reply import get_kb



async def get_start(message: Message, bot: Bot):
    await message.answer('Bienvenue au Quizz', reply_markup=get_kb())


async def get_queez(message: Message, bot: Bot):
    await message.answer('Qui dois-je appeler le roi du football', reply_markup=first_question_u7())
