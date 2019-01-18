import ssl
import aiohttp

from services.parser.modules import DATA_INFO


class Base(object):
    def __init__(self, data: dict, module_id: str):
        self.__module_id = module_id
        self.__data = data
        self.__result = {
            'id': module_id,
            'error': None,
            'data': {
                'BUY_USD': None,
                'BUY_EUR': None,
                'SELL_USD': None,
                'SELL_EUR': None,
            }
        }

    async def load_page(self) -> str:
        async with aiohttp.ClientSession() as session:
            body = await self.__fetch(session, self.info.get('url'))

        return body

    def update_currency(self, data: dict):
        self.__result['data'].update(data)

    def update_error(self, error: any):
        self.__result['error'] = str(error)

    @property
    def result(self) -> dict:
        return self.__result

    @property
    def info(self) -> dict:
        return DATA_INFO.get(self.__module_id, None)

    @staticmethod
    def usd_code() -> int:
        return 840

    @staticmethod
    def eur_code() -> int:
        return 978

    @staticmethod
    async def __fetch(session: aiohttp.ClientSession, url: str) -> str:
        ssl_client = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
        async with session.get(url, ssl=ssl_client) as response:
            return await response.text()
