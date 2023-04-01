from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from i18n import i18n_ru

router: Router = Router()

@router.message(CommandStart())
async def handle_start_command(message: Message):
    await message.answer(text=i18n_ru.start)

@router.message(Command(commands='help'))
async def handle_help_command(message: Message):
    await message.answer(text=i18n_ru.help)

@router.message()
async def handle_message(message: Message):
    try:
        #await message.answer(chat_id=message.chat.id)
        print(message.from_user)
        await message.answer(text=i18n_ru.default)
    except TypeError:
        await message.answer(text=i18n_ru.default)