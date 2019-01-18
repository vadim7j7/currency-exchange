import json

from services.parser.modules.base import Base


class Alfabank(Base):
    def __init__(self, data: dict):
        super(Alfabank, self).__init__(data, 'alfabank')

    async def start(self) -> dict:
        try:
            body = await self.load_page()
            data = json.loads(body)
        except Exception as error:
            self.update_error(error)
        else:
            data_usd = data.get('usd', {})
            data_eur = data.get('eur', {})

            self.update_currency({
                'BUY_USD': self.parse_value(data_usd, 'buy'),
                'SELL_USD': self.parse_value(data_usd, 'sell'),
                'BUY_EUR': self.parse_value(data_eur, 'buy'),
                'SELL_EUR': self.parse_value(data_eur, 'sell')
            })

        return self.result

    @staticmethod
    def parse_value(data: list, type_key: str) -> float or None:
        try:
            result = list(filter(
                lambda x: x['type'] == type_key, data))[0].get('value')
        except IndexError:
            pass
        else:
            if result is not None:
                return float(result)

        return None
