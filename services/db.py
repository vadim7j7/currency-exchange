import asyncpg

from setting import PgConfig
from services.parser.modules import DATA_INFO
from services.sql_queries import select_bank_by__id, insert_bank, update_bank, \
    select_current_currency_by_bank_id_and_code, insert_current_currency,\
    update_current_currency

pgConfig = PgConfig()


async def connect() -> asyncpg.connect:
    conn = await asyncpg.connect(dsn=pgConfig.dsn)
    return conn


async def sync_banks():
    conn = await connect()

    for _, item in DATA_INFO.items():
        bank = await conn.fetchrow(select_bank_by__id, item['id'])
        if bank is None:
            await conn.execute(insert_bank, item['id'], item['name'])
        elif not item['name'] == bank['name']:
            await conn.execute(update_bank, bank['id'], item['name'])

    await conn.close()


async def refresh_currencies(data: list):
    conn = await connect()

    for item in data:
        bank = await conn.fetchrow(select_bank_by__id, item['id'])
        if bank is not None:
            for key, val in item['data'].items():
                if val is None:
                    continue

                currency = await conn.fetchrow(
                    select_current_currency_by_bank_id_and_code,
                    bank['id'], key
                )
                if currency is None:
                    await conn.execute(
                        insert_current_currency,
                        bank['id'], key, val)
                elif not val == float(currency['value']):
                    await conn.execute(
                        update_current_currency,
                        currency['id'], val)

    await conn.close()
