from environs import Env
import asyncio
from aiogram import Bot, Dispatcher
from config import load_config
from handler import user_handler #,admin_handler
from keyboard.menu import set_menu

async def main() -> None:

    config = load_config('.env')

    bot: Bot = Bot(token=config.bot.token)
    dp: Dispatcher = Dispatcher()

    # Регистриуем роутеры в диспетчере
    dp.include_router(user_handler.router)
    #dp.include_router(admin_handler.router)

    await set_menu(bot)

    #await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())