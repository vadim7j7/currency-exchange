from aiohttp.web import Application, run_app

from api.handles.banks import all_banks
from api.handles.currency import all_currencies
from api.db import init_db, close_db


def main():
    app = Application()
    app.router.add_get('/api/v1/banks', all_banks)
    app.router.add_get('/api/v1/currencies', all_currencies)
    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)
    run_app(app=app)


if __name__ == '__main__':
    main()
