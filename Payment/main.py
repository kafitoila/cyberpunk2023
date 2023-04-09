from environs import Env
import asyncio
from aiogram import Bot, Dispatcher
from loguru import logger
# import uvloop  # running only linux

from config import load_config
from handler import admin_handler, user_handler
from keyboard.menu import set_menu
from db.database import Database


import asyncpg

# data_ = {}
# config = load_config('.env')
# c = config.db
# dsn = f'postgres://{c.db_user}:{c.db_password}@{c.db_host}:{c.db_port}'

# async def create_pool():
#     # data_['pool'] = await asyncpg.create_pool(dsn=dsn)
#     pool = await asyncpg.create_pool(dsn=dsn)
#     # data_["db"] = Database(pool)

async def main() -> None:

    config = load_config('.env')
    print(config.db)

    bot: Bot = Bot(token=config.bot.token,
                   parse_mode='MarkdownV2')

    db: Database = Database(
        name=config.db.database,
        user=config.db.db_user,
        password=config.db.db_password,
        host=config.db.db_host,
        port=config.db.db_port)

    async with asyncpg.create_pool(
        database=config.db.database,
        user=config.db.db_user,
        password=config.db.db_password,
        host=config.db.db_host,
        port=config.db.db_port,
        min_size=6,
        max_size=6) as pool:

        await db.create_user(pool)
        # await db.add_user(pool)

    # db: Database = Database(
    #     name=config.db.database,
    #     user=config.db.db_user,
    #     password=config.db.db_password,
    #     host=config.db.db_host,
    #     port=config.db.db_port,
    #     # pool = data_['pool'])
    #     pool = await asyncpg.create_pool(dsn=dsn))

    # await db.verification('123456')

    dp: Dispatcher = Dispatcher()

    # Регистриуем роутеры в диспетчере
    dp.include_router(admin_handler.router_adm)
    dp.include_router(user_handler.router)

    await set_menu(bot)

    #await bot.delete_webhook(drop_pending_updates=True)
    # await dp.startup.register(create_pool) # ANSWER
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())