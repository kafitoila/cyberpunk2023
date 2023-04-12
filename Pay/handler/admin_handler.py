from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, CommandObject, BaseFilter
from core.config import config
from i18n import i18n_ru


# Собственный фильтр, проверяющий юзера на админа
class IsAdmin(BaseFilter):
    def __init__(self, admins: list[int]) -> None:
        # В качестве параметра фильтр принимает список с целыми числами
        self.admins = config.bot.admins

    async def __call__(self, message: Message) -> bool:
        print(message.from_user.id)
        return message.from_user.id in self.admins

# def is_admin(id: int, admins):
#     if id in admins:
#         return True

router_adm: Router = Router()

router_adm.message.filter()

@router_adm.message(Command(commands='exit'))
async def handle_exit(message: Message):
    print('exit')
    exit()
    try:
        user=message.from_user
        # if is_admin(user.id, admins):
        #     dp.stop_polling()
        #     await dp.wait_closed()
    except TypeError:
        await message.answer(text=i18n_ru.default)

# Этот хэндлер будет срабатывать, если апдейт от админа
# @router_adm.message(IsAdmin(config.bot.admins))
# async def answer_if_admins_update(message: Message):
#     await message.answer(text='Вы админ')


# Этот хэндлер будет срабатывать, если апдейт не от админа
# @router_adm.message(~IsAdmin(config.bot.admins))
# async def answer_if_not_admins_update(message: Message):
#     await message.answer(text='Вы не админ')