from aiogram import Bot
from aiogram.types import BotCommand
from i18n import i18n_ru

async def set_menu(bot: Bot):
    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/help',
                   description=i18n_ru.menu_help),
        BotCommand(command='/start',
                   description=i18n_ru.menu_start),
        BotCommand(command='/pay',
                   description=i18n_ru.menu_pay),
        BotCommand(command='/balance',
                   description=i18n_ru.menu_balance)#,
        # BotCommand(command='/pay_from',
        #            description=i18n_ru.menu_pay_from),
        # BotCommand(command='/set_access',
        #            description=i18n_ru.menu_set_access),
        # BotCommand(command='/get_access',
        #            description=i18n_ru.menu_get_access)
        ]
    await bot.set_my_commands(main_menu_commands)

# async def set_main_menu(bot: Bot):
#     main_menu_commands = [BotCommand(
#                                 command=command,
#                                 description=description
#                           ) for command,
#                                 description in LEXICON_COMMANDS_RU.items()]
#     await bot.set_my_commands(main_menu_commands)