from pydantic_settings import BaseSettings


class Config(BaseSettings):
    dbuser: str = 'admin123'
    dbpassword: str = 'p0ssw0rd'
    dbhost: str = 'localhost'
    dbname: str = 'postgres'
    dbport: int = 5432
    reset_db: bool = False
    logging_level: str = 'debug'
    postgres_initdb_args: str = "-A md5"
    service_name: str = 'postgres'


    @property
    def db_url(self) -> str:
        return f'postgresql+asyncpg://{self.dbuser}:{self.dbpassword}@{self.dbhost}:{self.dbport}/{self.dbname}'


config = Config(_env_file='../.env', _env_file_encoding='utf-8')

