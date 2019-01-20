from json import dumps as json_dumps

from aiohttp.web import Response
from api.db import select_all_bank, select_all_currencies


async def all_currencies(request) -> Response:
    async with request.app['pool'].acquire() as connect:
        currencies = await connect.fetch(select_all_currencies)
        banks = await connect.fetch(select_all_bank)

        data = {}
        for currency in currencies:
            if data.get(currency['bank_id']) is None:
                data[currency['bank_id']] = {}
            data[currency['bank_id']][currency['code']] =\
                float(currency['value'])

        result = []
        for bank in banks:
            result.append({
                'bank': {
                    'id': bank['id'],
                    'key': bank['_id'],
                    'name': bank['name']
                },
                'currencies': data[bank['id']]
            })

        return Response(
            body=json_dumps(result),
            content_type='application/json'
        )
