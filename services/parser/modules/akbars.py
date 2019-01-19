import json

from services.parser.modules.base import Base


class Akbars(Base):
    def __init__(self, data: dict):
        super(Akbars, self).__init__(data, 'akbars')

    async def start(self) -> dict:
        try:
            body = await self.load_page()
            data = json.loads(body)
        except Exception as error:
            self.update_error(error)
            return self.result

        result = self.parse_json(data)
        if result is not None:
            self.update_currency(result)

        return self.result

    @staticmethod
    def parse_json(data: dict) -> dict:
        result = {}

        data_usd = list(filter(lambda x: x['currencyCode'] == 'USD', data))
        try:
            data_usd = data_usd[0]
        except IndexError:
            pass
        else:
            if data_usd:
                result['BUY_USD'] = data_usd.get('purchasePrice')
                result['SELL_USD'] = data_usd.get('salePrice')

        data_eur = list(filter(lambda x: x['currencyCode'] == 'EUR', data))
        try:
            data_eur = data_eur[0]
        except IndexError:
            pass
        else:
            if data_eur:
                result['BUY_EUR'] = data_eur.get('purchasePrice')
                result['SELL_EUR'] = data_eur.get('salePrice')

        return result
