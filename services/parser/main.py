import asyncio

from services.parser.modules import DATA_INFO
from utils import import_by_string


class Parser(object):
    def __init__(self, options: list, queues: int = 2):
        self.__options = options
        self.__result = []
        self.__q = asyncio.Queue(queues)

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.__start())
        loop.close()

    @property
    def result(self):
        return self.__result

    async def __start(self):
        consumer = asyncio.ensure_future(self.__consumer())

        await self.__producer()
        await self.__q.join()

        consumer.cancel()

    async def __consumer(self):
        while True:
            data = await self.__q.get()

            try:
                await self.__handler(data)
            except Exception as error:
                print(error)

            self.__q.task_done()

    async def __producer(self):
        for option in self.__options:
            await self.__q.put(option)

    # Run a module to send a record to the module of a networking
    async def __handler(self, data: dict):
        name = DATA_INFO.get(data.get('id'), {}).get('module', None)
        if name is not None:
            network_obj = import_by_string(name)
            network_module = network_obj(data)

            result = await network_module.start()
            self.__result.append(result)
