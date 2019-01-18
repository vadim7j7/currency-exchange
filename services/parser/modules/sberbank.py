import json

from services.parser.modules.base import Base


class Sberbank(Base):
    def __init__(self, data: dict):
        super(Sberbank, self).__init__(data, 'sberbank')

    async def start(self) -> dict:
        try:
            body = await self.load_page()
            data = json.loads(body)
        except Exception as error:
            self.update_error(error)
        else:
            data_usd = data.get('beznal', {}).get(str(self.usd_code()), {})\
                .get('0', {})
            data_eur = data.get('beznal', {}).get(str(self.eur_code()), {})\
                .get('0', {})

            self.update_currency({
                'BUY_USD': data_usd.get('buyValue'),
                'SELL_USD': data_usd.get('sellValue'),
                'BUY_EUR': data_eur.get('buyValue'),
                'SELL_EUR': data_eur.get('sellValue')
            })

        return self.result
