from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data.config import DB_USER, DB_PASS, DB_HOST, DB_NAME


class Postgres:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            database=DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetch_val: bool = False,
                      fetch_row: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetch_val:
                    result = await connection.fetchval(command, *args)
                elif fetch_row:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result


class Database(Postgres):
    async def add_user(self, user_id: int, lang: str) -> None:
        sql = "INSERT INTO users (user_id, lang) VALUES ($1 , $2)"
        await self.execute(sql, user_id, lang, execute=True)

    async def check_user(self, user_id: int) -> bool:
        sql = "SELECT * FROM users WHERE user_id = $1"
        result = await self.execute(sql, user_id, fetch_val=True)

        return bool(result)

    async def lang(self, user_id: int) -> str:
        sql = "SELECT lang FROM users WHERE user_id = $1"
        return await self.execute(sql, user_id, fetch_val=True)

db = Database()
