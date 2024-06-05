import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)

bot = Bot(token="7424637129:AAE2DPkKU20vzFkaUHALGXAZGu8bXH8W874")
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: Message) -> None:
    await message.answer("Здравствуйте, напишите мне сообщение!")
    
@dp.message()
async def echo_answer(message: Message) -> None:
    await message.send_copy(chat_id = message.chat.id)
    
async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main());