import asyncio
from sqlalchemy import MetaData, Table, Integer, String, Column, ForeignKey, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base 
from datetime import datetime

from app.database.connection import async_main


Base = declarative_base()

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
    entry = Column(Text(2048), nullable=False)


#asyncio.run(async_main())
