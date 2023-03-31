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

# Magic filters
F.photo                                    # Фильтр для фото
F.voice                                    # Фильтр для голосовых сообщений
F.content_type.in_({ContentType.PHOTO,
                    ContentType.VOICE,
                    ContentType.VIDEO})    # Фильтр на несколько типов контента
F.text == 'привет'                         # Фильтр на полное совпадение текста
F.text.startswith('привет')                # Фильтр на то, что текст сообщения начинается с 'привет'
~F.text.endswith('bot')                    # Инвертирование результата фильтра
lambda message: message.photo                        # Фильтр для фото
lambda message: message.voice                        # Фильтр для голосовых сообщений
lambda message: message.content_type in {ContentType.PHOTO,
                                         ContentType.VOICE,
                                         ContentType.VIDEO}   # Фильтр на несколько типов контента
lambda message: message.text == 'привет'             # Фильтр на полное совпадение текста
lambda message: message.text.startswith('привет')    # Фильтр на то, что текст сообщения начинается с 'привет'
lambda message: not message.text.startswith('bot')   # Инвертирование результата фильтра

lambda message: message.from_user.id == 173901673
F.from_user.id == 173901673                         # superuser only
lambda message: message.from_user.id in {193905674, 173901673, 144941561}
F.from_user.id.in_({193905674, 173901673, 144941561}) # admins only
lambda message: not message.text.startswith('Привет')
~F.text.startswith('Привет')
lambda message: not message.content_type in {ContentType.PHOTO,
                                             ContentType.VIDEO,
                                             ContentType.AUDIO,
                                             ContentType.DOCUMENT}
~F.content_type.in_({ContentType.PHOTO,
                     ContentType.VIDEO,
                     ContentType.AUDIO,
                     ContentType.DOCUMENT})

if __name__ == '__main__':
    dp.run_polling(bot)