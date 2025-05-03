from functools import lru_cache
from aiogram.enums import ParseMode
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath, SecretStr

#from pathlib import Path
#ROOD_DIR: DirectoryPath = Path(__file__).parent.parent

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

    def get_db_url(self):
        return (f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@"
                f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")


class Settings():
    bot: BotSettings = BotSettings()
    database: DatabaseSettings = DatabaseSettings()


settings = Settings() 

