from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from config import load_config
from i18n import i18n_ru

config = load_config('.env')
admins = config.bot.admins

def is_admin(id: int, admins):
    if id in admins:
        return True

router_adm: Router = Router()

# router_adm.message.filter(~Command(commands=['help','start']))
router_adm.message.filter(~Command(commands=['help','start','pay','911']))

@router_adm.message()
async def handle_message(message: Message):
    try:
        #await message.answer(chat_id=message.chat.id)
        user=message.from_user
        print(user)
        if is_admin(user.id, admins):
            await message.answer(text=f'{user.first_name} {user.last_name}, ты админ\!')
        else:
            await message.answer(text=f'{user.first_name} {user.last_name}, ты не админ\!')
    except TypeError:
        await message.answer(text=i18n_ru.default)