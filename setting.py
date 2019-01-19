from dataclasses import dataclass


@dataclass
class PgConfig:
    user: str = 'developer'
    password: str = 'developer'
    database: str = 'currency_exchange'
    host: str = '192.168.33.10'
    port: str = '5432'

    @property
    def dsn(self) -> str:
        return 'postgres://{user}:{password}@{host}:{port}/{database}'.format(
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database
        )
