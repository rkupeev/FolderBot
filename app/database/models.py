from sqlalchemy import Column, Integer, BigInteger, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs

from datetime import datetime


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True



class Users(Base):
    __tablename__ = "users"

    id = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    telegram_id = mapped_column(BigInteger, nullable=False)
    added_at = mapped_column(DateTime, default=datetime.now())

    #relationship one-to-many with Entity
    entities = relationship("Entities", back_populates="users")



class Entities(Base):
    __tablename__ = "entities"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id = mapped_column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = mapped_column(String(255), nullable=False)
    content = mapped_column(Text, nullable=False)
    created_at = mapped_column(DateTime, default=datetime.now())
    
    users = relationship("Users", back_populates="entities")

