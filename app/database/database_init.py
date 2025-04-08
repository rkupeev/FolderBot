
from app.database.connection import engine
from app.database.models import Base
import asyncio


async def init_db() -> None: 
    async with engine.begin() as conn:
        #await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(init_db())