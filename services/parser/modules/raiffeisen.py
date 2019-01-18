from bs4 import BeautifulSoup

from services.parser.modules.base import Base

TABLE_CLS = 'b-table b-table-currency'


class Raiffeisen(Base):
    def __init__(self, data: dict):
        super(Raiffeisen, self).__init__(data, 'raiffeisen')

    async def start(self) -> dict:
        try:
            html_data = await self.load_page()
        except Exception as error:
            self.update_error(error)
        else:
            result = self.parse_html(html_data)
            if result is not None:
                self.update_currency(result)

        return self.result

    @staticmethod
    def parse_html(html_data: str) -> dict or None:
        soup = BeautifulSoup(html_data, 'html.parser')
        table = soup.find_all('div', {'class': TABLE_CLS})
        if table is None:
            return None

        table = table[1]
        if table is None:
            return None

        temp = table.find_all(class_='b-table__td')
        if temp is None:
            return None

        result = {}
        if 'USD' in temp[7].text:
            result['BUY_USD'] = float(temp[10].text)
            result['SELL_USD'] = float(temp[12].text)

        if 'EUR' in temp[14].text:
            result['BUY_EUR'] = float(float(temp[17].text))
            result['SELL_EUR'] = float(float(temp[19].text))

        return result
