import asyncio

from services.db import sync_banks, refresh_currencies
from services.parser.main import Parser
from services.parser.modules import DATA_INFO


async def run():
    tmp = map(lambda key: {'id': DATA_INFO[key]['id']}, DATA_INFO)
    options_all_banks = list(tmp)
    parser = Parser(options_all_banks)
    await parser.start()

    await sync_banks()
    await refresh_currencies(parser.result)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.close()


if __name__ == "__main__":
    main()
