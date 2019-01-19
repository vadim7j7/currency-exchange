from bs4 import BeautifulSoup

from services.parser.modules.base import Base

TABLE_CLS = 'table table_simple table_nowrap'


class Otpbank(Base):
    def __init__(self, data: dict):
        super(Otpbank, self).__init__(data, 'otpbank')

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

        result = {}
        temp = table.find_all('td')
        if temp is None:
            return None

        if 'USD' in temp[3].text:
            result['BUY_USD'] = float(temp[4].text.replace(',', '.'))
            result['SELL_USD'] = float(temp[5].text.replace(',', '.'))

        if 'EUR' in temp[6].text:
            result['BUY_EUR'] = float(temp[7].text.replace(',', '.'))
            result['SELL_EUR'] = float(temp[8].text.replace(',', '.'))

        return result
