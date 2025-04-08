from sqlalchemy import Column, Integer, BigInteger, String, Text, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True



class User(Base):
    __tablename__ = "users"

    id = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    username = mapped_column(String(120), nullable=False, autoincrement=True)
    added_at = mapped_column(TIMESTAMP)

    #relationship one-to-many with Entity
    entities = relationship("Entity", back_populates="users")



class Entity(Base):
    __tablename__ = "entities"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id = mapped_column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = mapped_column(String(255), nullable=False)
    content = mapped_column(Text, nullable=False)
    created_at = mapped_column(TIMESTAMP)
    
    user = relationship("User", back_populates="entities")

