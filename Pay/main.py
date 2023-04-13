import asyncpg
import asyncio
import logging
import contextlib

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
# from aiogram.fsm.storage.redis import RedisStorage

from core.middlewares.dbmiddleware import DbSession
from db.database import Request
from core.config import config
from keyboard.menu import set_menu
from handler import user_handler, admin_handler
# from core.handlers import sender
# from core.utils.sender_list import SenderList
# from core.utils.sender_state import Steps


async def start_bot(bot: Bot):
    await set_menu(bot)
    await bot.send_message(config.bot.admins[0], text='Бот запущен!')


async def stop_bot(bot: Bot): #, dp: Dispatcher):
    await bot.send_message(config.bot.admins[0], text='Бот остановлен!')
    await bot.session.close()
    await bot.close()


async def create_pool():
    return await asyncpg.create_pool(user=config.db.db_user, password=config.db.db_password,
                                     database=config.db.database, host=config.db.db_host,
                                     port=config.db.db_port, command_timeout=60)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    # logging.basicConfig(level=logging.DEBUG,
    #                     format="%(asctime)s - [%(levelname)s] -  %(name)s - "
    #                            "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    #                     )
    bot = Bot(token=config.bot.token, parse_mode='HTML')
    pool_connect = await create_pool()

    # storage = RedisStorage.from_url('redis://localhost:6379/0')
    # dp = Dispatcher(storage=storage)
    dp = Dispatcher()

    dp.update.middleware.register(DbSession(pool_connect))
    dp.message.middleware(DbSession(pool_connect))
    # await Request.init(pool_connect)
    request = Request(pool_connect)
    await request.init()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.include_router(admin_handler.router_adm)
    dp.include_router(user_handler.router)

    # dp.message.register(sender.get_sender, Command(commands='sender', magic=F.args),
    #                     F.chat.id == config.bot.admins[0])
    # dp.message.register(sender.get_message, Steps.get_message, F.chat.id == config.bot.admins[0])
    # dp.callback_query.register(sender.sender_decide, F.data.in_(['confirm_sender', 'cancel_sender']))
    # dp.callback_query.register(sender.q_button, Steps.q_button)
    # dp.message.register(sender.get_text_button, Steps.get_text_button, F.chat.id == config.bot.admins[0])
    # dp.message.register(sender.get_url_button, Steps.get_url_button, F.chat.id == config.bot.admins[0], F.text)

    # sender_list = SenderList(bot, pool_connect)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        # await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), senderlist=sender_list)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), request=request)
    except Exception as ex:
        logging.error(f"[!!! Exception] - {ex}", exc_info=True)
    # finally:
        # dp.stop_pollin()
        # await dp.wait_closed()

if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(main())