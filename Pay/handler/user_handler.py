from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, BaseFilter, Text
from i18n import i18n_ru
from db.database import Request

class CodeInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[str]]:
        # Разрезаем сообщение по пробелам, проверяем
        msg = message.text.split()
        print(msg)
        if len(msg) > 1:
            return {'msg': msg}
        return False

router: Router = Router()

@router.message(CommandStart(),CodeInMessage())
async def handle_registration(message: Message, msg: list[str], request: Request):
    # check code exists in DB
    if await request.check_user_id_exists(msg[1]):
        print('Регистрация прошла успешно!')
    # check code is not already registered
    # register in DB
    # send greeting message
    await message.answer(text=msg[1])

@router.message(Text(contains='select', ignore_case=True))
@router.message(Text(contains='insert', ignore_case=True))
@router.message(Text(contains='values', ignore_case=True))
@router.message(Text(contains='drop', ignore_case=True))
@router.message(Text(contains='table', ignore_case=True))
@router.message(Text(contains='delete', ignore_case=True))
@router.message(Text(contains='update', ignore_case=True))
@router.message(Text(contains='alter', ignore_case=True))
@router.message(Text(contains='grant', ignore_case=True))
@router.message(Text(contains='from', ignore_case=True))
@router.message(Text(contains='into', ignore_case=True))
@router.message(Text(contains='where', ignore_case=True))
@router.message(Text(contains=';', ignore_case=True))
async def handle_sql_injection(message: Message, msg: list[str]):
    await message.answer(text=i18n_ru.sql_injection)

@router.message(CommandStart())
async def handle_start_command(message: Message):
    await message.answer(text=i18n_ru.start)

@router.message(Command(commands='help'))
async def handle_help_command(message: Message):
    await message.answer(text=i18n_ru.help)

@router.message(Command(commands='911'))
async def handle_911_command(message: Message):
    await message.answer('Травма в пути')

@router.message(Command(commands='pay'))
async def handle_pay_command(message: Message):
    await message.answer('Плати')

@router.message()
async def handle_message(message: Message):
    try:
        #await message.answer(chat_id=message.chat.id)
        print(message)
        await message.answer(text=i18n_ru.default)
    except TypeError:
        await message.answer(text=i18n_ru.default)