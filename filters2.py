from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command
from aiogram import F

token: str ='5665289787:AAHVqrTkOvkxMpJuylPtjwy7AXAGEq96r3g'
bot: Bot = Bot(token)
dp: Dispatcher = Dispatcher()

@dp.message(Text(endswith=['бот'], ignore_case=True))
async def process_text_endswith_bot(message: Message):
    await message.answer(text='Ваше сообщение заканчивается на бот')

@dp.message(Text(contains=['бот ', 'бот.', 'бот!', 'бот?',
                           'бота', 'боту', 'боте', 'ботом', 'боты'], ignore_case=True))
async def process_text_contains_bot(message: Message):
    await message.answer(text='Нет, я не бот!')

# Этот хэндлер будет срабатывать на команду "+hack"
@dp.message(Command(commands=['hack'], prefix='+'))
async def process_command_start_2(message: Message):
    await message.answer('Wow! '
                         'Real gangsta shit')

if __name__ == '__main__':
    dp.run_polling(bot)