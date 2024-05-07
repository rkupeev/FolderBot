import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from app.core import get_settings
from app.database.models import metadata 


async def create_tables():
    async_engine = create_async_engine(
        get_settings().database.DATABASE_URL_asyncpg
        )
    async_session = AsyncSession(async_engine)

    async with async_engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)

    await async_session.commit()
    await async_session.close()

asyncio.run(create_tables())
