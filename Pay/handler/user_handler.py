from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, BaseFilter, Text
from aiogram import F
from i18n import i18n_ru
from db.database import Request

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

router: Router = Router()

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

@router.message(CommandStart(),CodeInMessage())
async def handle_registration(message: Message, msg: list[str], request: Request):
    user_id = msg[1]
    # check code exists in DB
    if not await request.check_user_id_exists(user_id):
        await message.answer(text=i18n_ru.check_code)
    # check code is not already registered
    elif not await request.check_user_id_not_taken(user_id):
        await message.answer(text=i18n_ru.user_id_taken)
    # register in DB
    else:
        tg_id = message.from_user.id
        await request.register_user(tg_id,user_id)
        # send greeting message
        user_name = await request.get_user_name(tg_id)
        await message.answer(text=f'Привет, {user_name}!')
        await message.answer(text=i18n_ru.greeting)

@router.message(CommandStart())
async def handle_start_command(message: Message):
    await message.answer(text=i18n_ru.start)

@router.message(Command(commands='help'))
async def handle_help_command(message: Message):
    await message.answer(text=i18n_ru.help)

# @router.message((Command(commands='911')|Command(commands='tt')),CodeInMessage())
# async def handle_911_command(message: Message, msg: list[str], request: Request):
#     address = msg[1]
#     await message.answer(f'Травма в пути: {address}')

@router.message(Command(commands='pay'),CodeInMessage())
async def handle_pay_command(message: Message, msg: list[str], request: Request):
    tg_id = message.from_user.id
    # check tg_id assigned in DB
    if not await request.check_tg_id_assigned(tg_id):
        await message.answer(text=i18n_ru.tg_not_assigned)

    await message.answer('Плати')

@router.message()
async def handle_message(message: Message):
    await message.answer(text=i18n_ru.default)