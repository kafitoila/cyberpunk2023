from typing import List, Tuple, Any

import asyncpg
from asyncpg import Record


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def init(self):
        print('DB init')
        f = open("sql/init.sql", "r", encoding='UTF8')
        query1 = f.read()
        print(query1)
        # print(dir(self))
        await self.execute(query1)

    async def check_table(self, name_table):
        query = f"SELECT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = '{name_table}');"
        return await self.connector.fetchval(query)

    async def create_table(self, name_table):
        query = f"CREATE TABLE {name_table} (user_id bigint NOT NULL, statuse text, description text, PRIMARY KEY (user_id));"
        await self.connector.execute(query)
        query = f"INSERT INTO {name_table} (user_id, statuse, description) SELECT user_id, 'waiting', null FROM users WHERE statuse='member'"
        await self.connector.execute(query)

    async def delete_table(self, name_table):
        query = f"DROP TABLE {name_table};"
        await self.connector.execute(query)