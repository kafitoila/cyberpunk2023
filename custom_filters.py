from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter
from aiogram.types import Message

token: str ='5665289787:AAHVqrTkOvkxMpJuylPtjwy7AXAGEq96r3g'
bot: Bot = Bot(token)
dp: Dispatcher = Dispatcher()

# Список с ID администраторов бота. !!!Замените на ваш!!!
admins: list[int] = [499598131]


# Собственный фильтр, проверяющий юзера на админа
class IsAdmin(BaseFilter):
    def __init__(self, admins: list[int]) -> None:
        # В качестве параметра фильтр принимает список с целыми числами
        self.admins = admins

    async def __call__(self, message: Message) -> bool:
        print(message.from_user.id)
        return message.from_user.id in self.admins


# Этот хэндлер будет срабатывать, если апдейт от админа
@dp.message(IsAdmin(admins))
async def answer_if_admins_update(message: Message):
    await message.answer(text='Вы админ')


# Этот хэндлер будет срабатывать, если апдейт не от админа
@dp.message()
async def answer_if_not_admins_update(message: Message):
    await message.answer(text='Вы не админ')


if __name__ == '__main__':
    dp.run_polling(bot)