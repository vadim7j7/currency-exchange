from bs4 import BeautifulSoup

from services.parser.modules.base import Base

TABLE_CLS = 'brand-table brand-table_rate brand-table_light'
TABLE_CELL_CLS = 'brand-table__cell_body'


class Zenit(Base):
    def __init__(self, data: dict):
        super(Zenit, self).__init__(data, 'zenit')

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
        table = soup.find('div', {'class': TABLE_CLS})
        if table is None:
            return None

        result = {}
        temp = table.find_all(class_=TABLE_CELL_CLS)
        if temp is None:
            return None

        if temp[0].text == 'Доллары':
            result['BUY_USD'] = float(temp[1].text.replace(',', '.'))
            result['SELL_USD'] = float(temp[2].text.replace(',', '.'))

        if temp[3].text == 'Евро':
            result['BUY_EUR'] = float(temp[4].text.replace(',', '.'))
            result['SELL_EUR'] = float(temp[5].text.replace(',', '.'))

        return result
