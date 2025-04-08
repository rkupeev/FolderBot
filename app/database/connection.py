import asyncio
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine

from app.core.settings import get_settings
from app.database.models import Base


engine = create_async_engine(
    get_settings().database.get_db_url(),
    echo=True)

async_session = async_sessionmaker(engine,
                                   expire_on_commit=False)

