from environs import Env
from config import load_config


config = load_config('.env')
print(config.bot.token)
print(config.bot.admins[0])
print(config.db.db_user)