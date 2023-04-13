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

# @router.message((Command(commands='911')|Command(commands='tt')),CodeInMessage())
# async def handle_911_command(message: Message, msg: list[str], request: Request):
#     address = msg[1]
#     await message.answer(f'Травма в пути: {address}')

@router.message(Command(commands='pay'),CodeInMessage(), Text(startswith='/pay', ignore_case=True))
async def handle_pay_command(message: Message, msg: list[str], request: Request, bot: Bot):
    sender_tg_id = message.from_user.id
    # check tg_id assigned in DB
    sender_id = await request.get_user_id(sender_tg_id)
    if not sender_id:
        await message.answer(text=i18n_ru.tg_not_assigned)
    elif len(msg) < 4:
        await message.answer(text=i18n_ru.error_no_comment)
        await message.answer(text=i18n_ru.pay)
    elif not msg[1].isdigit():
        await message.answer(text=i18n_ru.error_receiver_code)
    elif msg[1] == sender_id:
        await message.answer(text=i18n_ru.error_sending_to_self)
    elif not msg[2].isdigit() or int(msg[2]) < 0:
        await message.answer(text=i18n_ru.error_sum)
        await message.answer(text=i18n_ru.pay)
    else:
        sender_balance = await request.get_balance(sender_id)
        command = msg.pop(0)
        receiver_id = msg.pop(0)
        sum = int(msg.pop(0))
        comment = (' ').join(msg)
        if sum > sender_balance:
            await message.answer(text=i18n_ru.error_no_money)
        else:
            # pay
            new_sender_balance = sender_balance - sum
            await request.set_balance(sender_id,new_sender_balance)

            receiver_balance = await request.get_balance(receiver_id)
            new_receiver_balance = receiver_balance + sum
            await request.set_balance(receiver_id,new_receiver_balance)
            # save transaction
            await request.set_transaction(sender_id,receiver_id,sum,comment)
            # notify sender
            sender_text = f'Отправлено {sum} эдди получателю {receiver_id} с комментарием {comment}'
            await message.answer(text=sender_text)
            # notify receiver
            receiver_text = f'Получено {sum} эдди от {sender_id} с комментарием {comment}'
            receiver_tg_id = await request.get_tg_id(receiver_id)
            await bot.send_message(receiver_tg_id, text=receiver_text)
            #notify admins
            sender_user_name = await request.get_user_name(sender_tg_id)
            receiver_user_name = await request.get_user_name(receiver_tg_id)
            admin_text = f'От {sender_user_name} поступило {sum} эдди для {receiver_user_name} с комментарием {comment}'
            await bot.send_message(config.bot.admins[0], text=admin_text)
            await bot.send_message(config.bot.admins[1], text=admin_text)

@router.message(Command(commands='pay'))
async def handle_pay_info(message: Message):
    await message.answer(text=i18n_ru.pay)

@router.message(Command(commands='balance'))
async def handle_balance_command(message: Message, request: Request):
    tg_id = message.from_user.id
    user_id = await request.get_user_id(tg_id)
    if not user_id:
        await message.answer(text=i18n_ru.tg_not_assigned)
    else:
        balance = await request.get_balance(user_id)
        await message.answer(text=balance)

@router.message(Command(commands='pay_from'))
async def handle_pay_from_command(message: Message, request: Request):
    # get orgs associated
    tg_id = message.from_user.id
    org = await request.get_org_by_tg_id(tg_id)
    print(org)


    await message.answer(text=i18n_ru.error_no_organization)

@router.message(Command(commands='get_access'))
async def handle_get_access_command(message: Message, request: Request):
    # get orgs associated
    tg_id = message.from_user.id
    org_name = await request.get_org_name_by_tg_id(tg_id)
    if org_name:
        text_org = f'Доступ ко счёту: {org_name}'
        await message.answer(text=text_org)
    else:
        await message.answer(text=i18n_ru.error_no_organization)

@router.message(Command(commands='set_access'))
async def handle_set_access_command(message: Message, request: Request):
    await message.answer(text=i18n_ru.error_no_organization)

@router.message()
async def handle_message(message: Message, bot: Bot):
    await message.answer(text=i18n_ru.default)