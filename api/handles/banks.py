from json import dumps as json_dumps

from aiohttp.web import Response

from utils import compact_result
from api.db import select_all_bank


async def all_banks(request) -> Response:
    async with request.app['pool'].acquire() as connect:
        records = await connect.fetch(select_all_bank)

        return Response(
            body=json_dumps(compact_result(records)),
            content_type='application/json'
        )
