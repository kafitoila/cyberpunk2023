from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

token: str ='5665289787:AAHVqrTkOvkxMpJuylPtjwy7AXAGEq96r3g'
bot: Bot = Bot(token = token)
dp: Dispatcher = Dispatcher()

@dp.message(Command(commands=["start"]))
async def handle_start_command(message: Message):
    answer: str = 'Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь'
    #await message.answer(answer)
    await bot.send_message(message.chat.id, answer)

@dp.message(Command(commands=['help']))
async def handle_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')

@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)