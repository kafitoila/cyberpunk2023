from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter
from aiogram.filters import Text, Command
from aiogram.types import Message
from aiogram import F
from aiogram.types import PhotoSize

token: str ='5665289787:AAHVqrTkOvkxMpJuylPtjwy7AXAGEq96r3g'
bot: Bot = Bot(token)
dp: Dispatcher = Dispatcher()

# Список с ID администраторов бота. !!!Замените на ваш!!!
admins: list[int] = [4995981310]


# Собственный фильтр, проверяющий юзера на админа
class IsAdmin(BaseFilter):
    def __init__(self, admins: list[int]) -> None:
        # В качестве параметра фильтр принимает список с целыми числами
        self.admins = admins

    async def __call__(self, message: Message) -> bool:
        print(message.from_user.id)
        return message.from_user.id in self.admins

@dp.message(F.photo[0].as_('photo_min'))
async def process_photo_send(message: Message, photo_min: PhotoSize):
    # внутри хэндлера можно работать с одним объектом (photo_min) уже без индексов
    print(photo_min)

# Этот фильтр будет проверять наличие неотрицательных чисел
# в сообщении от пользователя, и передавать в хэндлер их список
class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = []
        # Разрезаем сообщение по пробелам, нормализуем каждую часть, удаляя
        # лишние знаки препинания и невидимые символы, проверяем на то, что
        # в таких словах только цифры, приводим к целым числам
        # и добавляем их в список
        for word in message.text.split():
            normalized_word = word.replace('.', '').replace(',', '').strip()
            if normalized_word.isdigit():
                numbers.append(int(normalized_word))
        # Если в списке есть числа - возвращаем список по ключу 'numbers'
        if numbers:
            return {'numbers': numbers}
        return False

# Этот хэндлер будет срабатывать, если сообщение пользователя
# начинается с фразы "найди числа" и в нем есть числа
@dp.message(Text(startswith='найди числа', ignore_case=True),
            NumbersInMessage())
# Помимо объекта типа Message, принимаем в хэндлер список чисел из фильтра
async def process_if_numbers(message: Message, numbers: list[int]):
    await message.answer(
            text=f'Нашел: {str(", ".join(str(num) for num in numbers))}')


# Этот хэндлер будет срабатывать, если сообщение пользователя
# начинается с фразы "найди числа", но в нем нет чисел
@dp.message(Text(startswith='привет', ignore_case=True))
@dp.message(Text(startswith='найди числа', ignore_case=True))
@dp.message(Text(startswith='найди числа', ignore_case=True) | Text(startswith='привет', ignore_case=True))
async def process_if_not_numbers(message: Message):
    await message.answer(
            text='Не нашел что-то :(')

# Этот хэндлер будет срабатывать, если апдейт от админа
@dp.message(IsAdmin(admins))
async def answer_if_admins_update(message: Message):
    await message.answer(text='Вы админ')


# Этот хэндлер будет срабатывать, если апдейт не от админа
@dp.message(~IsAdmin(admins))
async def answer_if_not_admins_update(message: Message):
    await message.answer(text='Вы не админ')


if __name__ == '__main__':
    dp.run_polling(bot)