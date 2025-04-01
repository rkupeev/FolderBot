import asyncio
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine

from app.core.settings import get_settings
from app.database.models import Base

async def create_session() -> None:
    engine = create_async_engine(
        get_settings().database.DATABASE_URL_asyncpg,
        echo=True
    )

    #async_session = async_sessionmaker(engine, expire_on_commit=False)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


asyncio.run(create_session())



