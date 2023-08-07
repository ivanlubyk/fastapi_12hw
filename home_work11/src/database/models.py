from sqlalchemy import Column, Integer, String, DateTime, func, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, date

from src.database.db import Base


class Contact(Base):
    __tablename__ = "contacts" # noqa
    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    first_name: Mapped[str] = Column(String, index=True)
    last_name: Mapped[str] = Column(String, index=True)
    email: Mapped[str] = Column(String, unique=True, index=True)
    phone: Mapped[str] = Column(String)
    birthday: Mapped[str] = Column(Date)
    created_at: Mapped[int] = Column(DateTime, default=func.now())
    user_id: Mapped[int] = Column('user_id', ForeignKey('users.id', ondelete='CASCADE'), default=None)
    user: Mapped["User"] = relationship('User', backref="users")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username: Mapped[str] = Column(String(50))
    email: Mapped[str] = Column(String(250), nullable=False, unique=True)
    password: Mapped[str] = Column(String(255), nullable=False)
    created_at: Mapped[date] = Column('crated_at', DateTime, default=func.now())
    update_at: Mapped[date] = Column('update_at', DateTime, default=func.now(), onupdate=func.now())
    avatar: Mapped[str] = Column(String(255), nullable=True)
    refresh_token: Mapped[str] = Column(String(255), nullable=True)