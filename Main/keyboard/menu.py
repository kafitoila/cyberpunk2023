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
        BotCommand(command='/911',
                   description=i18n_ru.menu_911),
        BotCommand(command='/police',
                   description=i18n_ru.menu_police),
        BotCommand(command='/me',
                   description=i18n_ru.me),
        BotCommand(command='/drugs',
                   description=i18n_ru.menu_drugs),
        BotCommand(command='/terminal',
                   description=i18n_ru.menu_terminal),
        # BotCommand(command='/implant',
        #            description=i18n_ru.menu_implant),
        # BotCommand(command='/insurance',
        #            description=i18n_ru.menu_insurance),
        # BotCommand(command='/ripper',
        #            description=i18n_ru.menu_ripper)
        ]
    await bot.set_my_commands(main_menu_commands)

# async def set_main_menu(bot: Bot):
#     main_menu_commands = [BotCommand(
#                                 command=command,
#                                 description=description
#                           ) for command,
#                                 description in LEXICON_COMMANDS_RU.items()]
#     await bot.set_my_commands(main_menu_commands)