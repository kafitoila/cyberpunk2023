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

class CodeInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[str]]:
        # Разрезаем сообщение по пробелам, проверяем
        msg = message.text.split()
        if len(msg) > 1:
            return {'msg': msg}
        return False

class TextInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[str]]:
        # Разрезаем сообщение по пробелам, проверяем
        msg = message.text.split()
        if len(msg) > 2:
            return {'msg': msg}
        return False

router_adm: Router = Router()

router_adm.message.filter(IsAdmin(config.bot.admins))
# Этот хэндлер будет срабатывать, если апдейт от админа

@router_adm.message(Command(commands='send_all'),CodeInMessage())
async def handle_send_all_command(message: Message):
    await message.answer(text=message.text)

@router_adm.message(Command(commands='send_all'))
async def handle_send_all_menu(message: Message):
    text = f'{i18n_ru.menu_send_all}\n\n{i18n_ru.send_all}'
    await message.answer(text=text)

@router_adm.message(Command(commands='send'),TextInMessage())
async def handle_send_command(message: Message):
    await message.answer(text=message.text)

@router_adm.message(Command(commands='send'))
async def handle_send_menu(message: Message):
    text = f'{i18n_ru.menu_send}\n\n{i18n_ru.send}'
    await message.answer(text=text)
