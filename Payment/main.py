from environs import Env
import asyncio
from aiogram import Bot, Dispatcher
from loguru import logger
# import uvloop  # running only linux

from config import load_config
from handler import admin_handler, user_handler
from keyboard.menu import set_menu
from db.database import Database

async def main() -> None:

    config = load_config('.env')

    bot: Bot = Bot(token=config.bot.token,
                   parse_mode='MarkdownV2')
    dp: Dispatcher = Dispatcher()

    # asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()

    db: Database = Database(
        name=config.db.database,
        user=config.db.db_user,
        password=config.db.db_password,
        host=config.db.db_host,
        port=config.db.db_port,
        loop=loop)

    await db.init()

    # Регистриуем роутеры в диспетчере
    dp.include_router(admin_handler.router_adm)
    dp.include_router(user_handler.router)

    await set_menu(bot)

    #await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())