from aiohttp.web import Application
from asyncpg import create_pool
from asyncpg.pool import Pool

from setting import PgConfig

pgConfig = PgConfig()


async def init_db(app: Application) -> Pool:
    pool = await create_pool(dsn=pgConfig.dsn)
    app['pool'] = pool

    return pool


async def close_db(app: Application):
    await app['pool'].close()


select_all_bank = '''SELECT * FROM banks;'''
select_all_currencies = '''SELECT * FROM current_currencies;'''
