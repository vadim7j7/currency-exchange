import json

from services.parser.modules.base import Base


class Vtb(Base):
    def __init__(self, data: dict):
        super(Vtb, self).__init__(data, 'vtb')

    async def start(self) -> dict:
        try:
            body = await self.load_page()
            data = json.loads(body)
        except Exception as error:
            self.update_error(error)
            return self.result

        result = {}

        try:
            data_usd = data.get('MoneyRates', [])[0]
        except IndexError:
            pass
        else:
            result['BUY_USD'] = data_usd.get('BankBuyAt')
            result['SELL_USD'] = data_usd.get('BankSellAt')

        try:
            data_eur = data.get('MoneyRates', [])[1]
        except IndexError:
            pass
        else:
            result['BUY_EUR'] = data_eur.get('BankBuyAt')
            result['SELL_EUR'] = data_eur.get('BankSellAt')

        self.update_currency(result)

        return self.result
