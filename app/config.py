from dataclasses import dataclass
from os import getenv


@dataclass
class Config:
    token: str

def load_config():
    return Config(token=getenv("BOT_TOKEN"))