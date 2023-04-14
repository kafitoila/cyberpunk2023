from aiogram import Router
from aiogram import Bot
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, BaseFilter, Text
from aiogram import F
from core.config import config
from i18n import i18n_ru
from db.database import Request

admins = config.bot.admins

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

async def do_default(message: Message, bot: Bot, request: Request):
    tg_id = message.from_user.id
    user_id = await request.get_user_id(tg_id)
    user_name = await request.get_user_name(tg_id)
    text = f'ECHO {tg_id}, {user_name}, {user_id}: {message.text}'
    await bot.send_message(config.bot.admins[0], text=text)
    await bot.send_message(config.bot.admins[1], text=text)

async def send_orgs(text: str, bot: Bot):
    await bot.send_message(config.bot.admins[0], text=text)
    await bot.send_message(config.bot.admins[1], text=text)

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
@router.message(Text(contains='into', ignore_case=True))
@router.message(Text(contains='where', ignore_case=True))
@router.message(Text(contains=';', ignore_case=True))
async def handle_sql_injection(message: Message, msg: list[str]):
    await message.answer(text=i18n_ru.sql_injection)

@router.message(CommandStart(),CodeInMessage())
async def handle_registration(message: Message, msg: list[str], request: Request, bot: Bot):
    await bot.send_message(config.bot.admins[0], text=message.text)
    await bot.send_message(config.bot.admins[1], text=message.text)
    user_id = msg[1]
    tg_id = message.from_user.id
    # check code exists in DB
    if not await request.check_user_id_exists(user_id):
        await message.answer(text=i18n_ru.check_code)
    # check code is not already registered
    elif not await request.check_user_id_not_taken(user_id):
        # register in DB
        print('register_user')
        await request.register_user(tg_id,user_id)
        # send greeting message
        user_name = await request.get_user_name(tg_id)
        await message.answer(text=f'Привет, {user_name}!')
        await message.answer(text=i18n_ru.greeting)
        await bot.send_message(config.bot.admins[0], text=f'{user_name} зарегистрировался')
        await bot.send_message(config.bot.admins[1], text=f'{user_name} зарегистрировался')
    else:
        taken_tg_id = await request.get_tg_id(user_id)
        if taken_tg_id == tg_id:
            user_name = await request.get_user_name(tg_id)
            await message.answer(text=f'Привет, {user_name}!')
            await message.answer(text=i18n_ru.already_registered)
        else:
            await message.answer(text=i18n_ru.user_id_taken)

@router.message(CommandStart())
async def handle_start_command(message: Message, request: Request):
    tg_id = message.from_user.id
    user_id = await request.get_user_id(tg_id)
    if user_id:
        user_name = await request.get_user_name(tg_id)
        text = f'Привет, {user_name}!\n\n{i18n_ru.already_registered}'
        await message.answer(text=text)
    else:
        await message.answer(text=i18n_ru.start)

@router.message(Command(commands='help'))
async def handle_help_command(message: Message):
    await message.answer(text=i18n_ru.help)

@router.message(Command(commands='911'),CodeInMessage())
async def handle_911_command(message: Message, msg: list[str], bot: Bot, request: Request):
    # await bot.send_message(config.bot.admins[0], text=text)
    # await bot.send_message(config.bot.admins[1], text=text)
    insurance = await request.get_insurance(message.from_user.id)
    if insurance == 'Платина' or insurance == 'Золото':
        command = msg.pop(0)
        address = (' ').join(msg)
        await message.answer(f'Травма в пути: {address}')
        text = f'Вызов ТТ по адресу: {address}'
        await bot.send_message(config.bot.admins[0], text=text)
        await bot.send_message(config.bot.admins[1], text=text)
        await bot.send_message(config.bot.admins[3], text=text)
    elif insurance == 'Серебро':
        text = 'У вас серебрянная страховка, Травма не приедет'
        await message.answer(text)
    else:
        text = 'Сожалеем, но у вас нет страховки'
        await message.answer(text)

@router.message(Command(commands='911'))
async def handle_911_menu(message: Message):
    text = f'{i18n_ru.menu_911}\n\n{i18n_ru.call911}'
    await message.answer(text=text)

@router.message(Command(commands='police'),CodeInMessage())
async def handle_police_command(message: Message, msg: list[str], bot: Bot, request: Request):
    await do_default(message, bot, request)
    command = msg.pop(0)
    address = (' ').join(msg)
    await message.answer(f'Полиция получила вызов: {address}')

@router.message(Command(commands='police'))
async def handle_police_menu(message: Message):
    text = f'{i18n_ru.menu_police}\n\n{i18n_ru.police}'
    await message.answer(text=text)

@router.message(Command(commands='drugs'),CodeInMessage())
async def handle_drugs_command(message: Message, msg: list[str], bot: Bot, request: Request):
    await do_default(message, bot, request)

@router.message(Command(commands='drugs'))
async def handle_drugs_menu(message: Message):
    text = f'{i18n_ru.menu_drugs}\n\n{i18n_ru.drugs}'
    await message.answer(text=text)

@router.message(Command(commands='terminal'),CodeInMessage())
async def handle_terminal_command(message: Message, msg: list[str], bot: Bot, request: Request):
    await do_default(message, bot, request)

@router.message(Command(commands='terminal'))
async def handle_terminal_menu(message: Message):
    text = f'{i18n_ru.menu_terminal}\n\n{i18n_ru.terminal}'
    await message.answer(text=text)

@router.message(Command(commands='implant'),TextInMessage())
async def handle_implant_command(message: Message, msg: list[str], bot: Bot, request: Request):
    await do_default(message, bot, request)

@router.message(Command(commands='implant'))
async def handle_implant_menu(message: Message):
    text = f'{i18n_ru.menu_implant}\n\n{i18n_ru.implant}'
    await message.answer(text=text)

@router.message(Command(commands='insurance'),TextInMessage())
async def handle_insurance_command(message: Message, msg: list[str], bot: Bot, request: Request):
    await do_default(message, bot, request)

@router.message(Command(commands='insurance'))
async def handle_insurance_menu(message: Message):
    text = f'{i18n_ru.menu_insurance}\n\n{i18n_ru.insurance}'
    await message.answer(text=text)

@router.message(Command(commands='ripper'),TextInMessage())
async def handle_ripper_command(message: Message, msg: list[str], bot: Bot, request: Request):
    await do_default(message, bot, request)

@router.message(Command(commands='ripper'))
async def handle_ripper_menu(message: Message):
    text = f'{i18n_ru.menu_ripper}\n\n{i18n_ru.ripper}'
    await message.answer(text=text)

@router.message(Command(commands='hack'),TextInMessage())
async def handle_hack_command(message: Message, msg: list[str], bot: Bot, request: Request):
    await do_default(message, bot, request)

@router.message(Command(commands='hack'))
async def handle_hack_menu(message: Message):
    text = f'{i18n_ru.menu_hack}\n\n{i18n_ru.hack}'
    await message.answer(text=text)

@router.message(Command(commands='me'))
async def handle_me_command(message: Message, request: Request):
    tg_id = message.from_user.id
    user_id = await request.get_user_id(tg_id)
    secret_id = await request.get_secret_id(tg_id)
    user_name = await request.get_user_name(tg_id)
    insurance = await request.get_insurance(message.from_user.id)
    text = f'Имя: {user_name}\n' \
        f'Открытый код: {user_id}\n' \
        f'Скрытый код: {secret_id}\n' \
        f'Страховка: {insurance}\n'
    await message.answer(text=text)

@router.message()
async def handle_message(message: Message, bot: Bot, request: Request):
    await do_default(message, bot, request)