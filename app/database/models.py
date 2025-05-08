from sqlalchemy import Integer, BigInteger, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy.ext.asyncio import AsyncAttrs

from datetime import datetime


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True



class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    added_at: Mapped[DateTime]= mapped_column(DateTime, default=datetime.now())

    #relationship one-to-many with Entity
    entities: Mapped[list["Entities"]] = relationship("Entities", back_populates="users")



class Entities(Base):
    __tablename__ = "entities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str] = mapped_column(String(2048), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    
    users: Mapped["Users"] = relationship("Users", back_populates="entities")

