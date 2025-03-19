
from functools import lru_cache
#from pathlib import Path
from aiogram.enums import ParseMode
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath, SecretStr

#ROOT_DIR: DirectoryPath = Path(__file__).parent.parent

class BotSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=f'/.env', env_file_encoding='utf-8')
    BOT_TOKEN: SecretStr
    PARSE_MOD: ParseMode | str = ParseMode.HTML

class DatabaseSettings(BaseSettings): 
    model_config = SettingsConfigDict(env_file=f'/.env', env_file_encoding='utf-8')
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL_asyncpg(self):
        # postgresql+asyncpg://postgres:postgres@localhost:5432/sa
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


class Settings():
    bot: BotSettings = BotSettings()
    database: DatabaseSettings = DatabaseSettings()


@lru_cache
def get_settings() -> Settings:
    return Settings()

