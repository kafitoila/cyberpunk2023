from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F

token: str ='5665289787:AAHVqrTkOvkxMpJuylPtjwy7AXAGEq96r3g'
bot: Bot = Bot(token = token)
dp: Dispatcher = Dispatcher()

async def handle_start_command(message: Message):
    answer: str = 'Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь'
    #await message.answer(answer)
    await bot.send_message(message.chat.id, answer)

async def handle_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')

async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)

async def send_echo(message: Message):
    await message.reply(text=message.text)

dp.message.register(handle_start_command, Command(commands=["start"]))
dp.message.register(handle_help_command,  Command(commands=['help']))
dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)