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
        await self.execute(query1)

    async def check_user_id_exists(self, user_id):
        query = f"SELECT EXISTS (SELECT 1 FROM users WHERE user_id = {user_id});"
        return await self.connector.fetchval(query)

    async def check_user_id_not_taken(self, user_id):
        query = f"SELECT EXISTS (SELECT 1 FROM users WHERE user_id = {user_id} AND tg_id <> 0);"
        return await self.connector.fetchval(query)

    async def check_tg_id_assigned(self, tg_id):
        query = f"SELECT EXISTS (SELECT 1 FROM users WHERE tg_id = {tg_id});"
        return await self.connector.fetchval(query)

    async def register_user(self, tg_id, user_id):
        query = f"UPDATE users SET tg_id = {tg_id} WHERE user_id = {user_id};"
        await self.connector.execute(query)

    async def get_user_name(self, tg_id):
        query = f"SELECT user_name FROM users WHERE tg_id = {tg_id};"
        return await self.connector.fetchval(query)

    async def get_tg_id(self, user_id):
        query = f"SELECT tg_id FROM users WHERE user_id = {user_id};"
        return await self.connector.fetchval(query)

    async def get_user_id(self, tg_id):
        query = f"SELECT user_id FROM users WHERE tg_id = {tg_id};"
        return await self.connector.fetchval(query)

    async def get_balance(self, user_id):
        query = f"SELECT balance FROM accounts WHERE user_id = {user_id};"
        return await self.connector.fetchval(query)

    async def set_balance(self, user_id, balance):
        query = f"UPDATE accounts SET balance = {balance} WHERE user_id = {user_id};"
        await self.connector.execute(query)

    async def set_transaction(self, sender_id, receiver_id, sum, comment):
        query = f"INSERT INTO transactions (sender_id, receiver_id, amount, comment) VALUES ({sender_id}, {receiver_id}, {sum}, '{comment}');"
        await self.connector.execute(query)

    async def get_org_name_by_user_id(self, user_id):
        query = f"select org_name from organizations where user_id = {user_id};"
        return await self.connector.fetchval(query)

    async def get_org_name_by_tg_id(self, tg_id):
        query = f"select o.org_name from organizations as o " \
        f"join users as u on o.user_id = u.user_id " \
        f"where u.tg_id = {tg_id};"
        return await self.connector.fetchval(query)

    async def get_org_by_tg_id(self, tg_id):
        query = f"select o.org_name, o.account_id from organizations as o " \
        f"join users as u on o.user_id = u.user_id " \
        f"where u.tg_id = {tg_id};"
        return await self.connector.fetchval(query)