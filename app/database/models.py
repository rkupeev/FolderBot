#import asyncio
from sqlalchemy import MetaData, Table, Integer, String, Column, ForeignKey, DateTime, CHAR
from sqlalchemy.orm import declarative_base 
from datetime import datetime

Base = declarative_base()
metadata = MetaData()
Base.metadata = metadata


class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, nullable=False, unique=True)
    reg_date = Column(DateTime(), default=datetime.now)


class Entries(Base):
    __tablename__ = 'entries'
    entry_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    heading = Column(CHAR(128), nullable=False)
    entry = Column(CHAR(2048), nullable=False)

