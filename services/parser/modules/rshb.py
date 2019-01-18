from bs4 import BeautifulSoup

from services.parser.modules.base import Base

TABLE_CLS = 'b-quotes-table'


class Rshb(Base):
    def __init__(self, data: dict):
        super(Rshb, self).__init__(data, 'rshb')

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
        table = soup.find('table', {'class': TABLE_CLS})
        if table is None:
            return None

        temp = table.find_all('td')
        if temp is None:
            return None

        result = {}
        if 'USD' in temp[0].text:
            result['BUY_USD'] = float(temp[1].text.strip())
            result['SELL_USD'] = float(temp[2].text.strip())

        if 'EUR' in temp[6].text:
            result['BUY_EUR'] = float(temp[7].text.strip())
            result['SELL_EUR'] = float(temp[8].text.strip())

        return result
