# 7302084975:AAEPi7jaA_Ipo80pjHAPuaqLb6xa9h1ZwLo
from aiogram import Bot, Dispatcher, html
from aiogram import filters
import asyncio
from config import *
from keyboards import *
from text import *

bot = Bot(token=API)


class Memorystorage:
    pass


dp = Dispatcher(bot, storage= Memorystorage())

@dp.message(commands=['start'])
async def starter(message):
    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}!")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)