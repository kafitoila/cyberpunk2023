from asyncio import AbstractEventLoop
from loguru import logger
from typing import Optional

import asyncpg


class Database:
    def __init__(
        self,
        name: Optional[str],
        user: Optional[str],
        password: Optional[str],
        host: Optional[str],
        port: Optional[str]
        # pool: asyncpg.create_pool
        # loop: AbstractEventLoop,
    ) -> None:
        self.name = name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        # self.pool = pool
        # self.loop = loop
        # self.pool = loop.run_until_complete(
        # self.pool = asyncpg.create_pool(
        #     database=name,
        #     user=user,
        #     password=password,
        #     host=host,
        #     port=port,
            # )
        # )

    # async def init(self) -> None:
    #     """create tables in the database."""
    #     # with open("Payment/sql/init.sql", "r") as f:
    #     print(dir(self))
    #     with open("sql/init.sql", "r") as f:
    #         sql = f.read()
    #     await self.pool.execute(sql)
    #     logger.info('Initialize DB')

    # async def close_database(self) -> None:
    #     await self.pool.close()

    # async def add_user(self, user_id: int, name: str, lang: str) -> None:
    #     """add a new user to the database."""
    #     await self.pool.execute(f"INSERT INTO Users VALUES({user_id}, '{name}', '{lang}')")
    #     logger.info(f"added new user | user_id: {user_id}; name: {name}; language: {lang}")

    # async def verification(self, user_id: int) -> bool:
    #     """checks if the user is in the database."""
    #     response = await self.pool.fetchrow(f"SELECT EXISTS(SELECT user_id FROM Users WHERE user_id={user_id})")
    #     return True if response else False

    # async def get_name(self, user_id: int) -> str:
    #     return await self.pool.fetchval(f"SELECT name FROM Users WHERE user_id={user_id}")

    # async def get_lang(self, user_id: int) -> str:
    #     return await self.pool.fetchval(f"SELECT lang FROM Users WHERE user_id={user_id}")

    async def create_user(self, pool):
        create_query = 'CREATE TABLE IF NOT EXISTS users ( user_id INTEGER PRIMARY KEY, secret_id CHAR(6));'
        async with pool.acquire() as connection:
            return await connection.execute(create_query)

    async def add_user(self, pool):
        user_id = 123457
        secret_id = 'QWE127'
        insert_query = f"INSERT INTO users (user_id, secret_id) VALUES ({user_id}, '{secret_id}');"
        async with pool.acquire() as connection:
            return await connection.execute(insert_query)

    async def add_user1(self, pool):
        user_id = 111112
        secret_id = 'QWE112'
        insert_query = f"INSERT INTO users (user_id, secret_id) VALUES ({user_id}, '{secret_id}');"
        async with pool.acquire() as connection:
            return await connection.execute(insert_query)