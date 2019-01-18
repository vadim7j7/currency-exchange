DATA_INFO = {
    'sberbank': {
        'id': 'sberbank',
        'name': 'Сбербанк',
        'module': 'services.parser.modules.sberbank.Sberbank',
        'url': 'https://www.sberbank.ru/portalserver/proxy/?pipe=shortCachePipe&url=http://localhost/rates-web/rateService/rate/current%3FregionId%3D55%26currencyCode%3D840%26currencyCode%3D978%26rateCategory%3Dbeznal'
    },
    'alfabank': {
        'id': 'alfabank',
        'name': 'Альфа - Банк',
        'module': 'services.parser.modules.alfabank.Alfabank',
        'url': 'https://alfabank.ru/ext-json/0.2/exchange/cash?offset=0&limit=2&mode=rest'
    },
    'zenit': {
        'id': 'zenit',
        'name': 'Банк Зенит',
        'module': 'services.parser.modules.zenit.Zenit',
        'url': 'https://www.zenit.ru/currency/'
    },
    'rshb': {
        'id': 'rshb',
        'name': 'Россельхозбанк',
        'module': 'services.parser.modules.rshb.Rshb',
        'url': 'https://www.rshb.ru/'
    },
    'raiffeisen': {
        'id': 'raiffeisen',
        'name': 'Райффайзенбанк Банк',
        'module': 'services.parser.modules.raiffeisen.Raiffeisen',
        'url': 'https://www.raiffeisen.ru/currency_rates/'
    }
}