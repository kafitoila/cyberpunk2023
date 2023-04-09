from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    database: str         # Название базы данных
    db_host: str          # URL-адрес базы данных
    db_user: str          # Username пользователя базы данных
    db_password: str      # Пароль к базе данных
    db_port: str


@dataclass
class Bot:
    token: str            # Токен для доступа к телеграм-боту
    admins: list[int]     # Список id администраторов бота


@dataclass
class Config:
    bot: Bot
    db: DatabaseConfig

# Создаем экземпляр класса Config и наполняем его данными из переменных окружения
def load_config(path: str | None) -> Config:

    env: Env = Env()
    env.read_env(path)

    return Config(bot=Bot(token=env('TOKEN'),
                          admins=list(map(int, env.list('ADMINS')))),
                  db=DatabaseConfig(database=env('DATABASE'),
                                    db_host=env('DB_HOST'),
                                    db_user=env('DB_USER'),
                                    db_password=env('DB_PASSWORD'),
                                    db_port=env('DB_PORT')))

config = load_config('.env')