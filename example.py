from services.parser.main import Parser

parser = Parser([
    {'id': 'sberbank'},
    {'id': 'alfabank'},
    {'id': 'zenit'},
    {'id': 'rshb'},
    {'id': 'raiffeisen'},
    {'id': 'vtb'},
    {'id': 'otpbank'},
    {'id': 'akbars'},
])

parser.run()


for bank in parser.result:
    print(bank)
