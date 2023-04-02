from environs import Env
import asyncio
from aiogram import Bot, Dispatcher
from config import load_config
from handler import admin_handler, user_handler
from keyboard.menu import set_menu

async def main() -> None:

    config = load_config('.env')

    bot: Bot = Bot(token=config.bot.token,
                   parse_mode='MarkdownV2')
    dp: Dispatcher = Dispatcher()

    # Регистриуем роутеры в диспетчере
    dp.include_router(admin_handler.router_adm)
    dp.include_router(user_handler.router)

    await set_menu(bot)

    #await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())