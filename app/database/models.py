import asyncio
from sqlalchemy import MetaData, Table, Integer, String, Column, ForeignKey, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from datetime import datetime

from app.core import get_settings

metadata = MetaData()

async def async_main():
    engine = create_async_engine(
        get_settings().database.DATABASE_URL_asyncpg
        )
    async with engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)

asyncio.run(async_main())












'''Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, nullable=False, unique=True)
    reg_date = Column(DateTime(), default=datetime.now)


class Entries(Base):
    __tablename__ = 'entries'
    entry_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    heading = Column(Text(128), nullable=False)
    entry = Column(Text(2048), nullable=False)'''
