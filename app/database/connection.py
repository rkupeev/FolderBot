from sqlalchemy.ext.asyncio import create_async_engine

from app.core.settings import get_settings

def create_engine():
    async_engine = create_async_engine(get_settings().database.DATABASE_URL_asyncpg)
    return async_engine


