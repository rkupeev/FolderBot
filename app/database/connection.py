from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.core.settings import get_settings


engine = create_async_engine(
    get_settings().database.get_db_url(),
    echo=True)

async_session_maker = async_sessionmaker(engine,
                                   expire_on_commit=False)

def connection(func):
    async def wrapper(*args, **kwargs):
        async with async_session_maker() as session:
            try:
                return await func(*args, session=session, **kwargs)
            except Exception as e:
                await session.rollback() #откат сессии
                raise e
            finally: 
                await session.close()
    return wrapper

