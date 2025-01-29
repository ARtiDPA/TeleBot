"""Файл моделей для бд."""
from sqlalchemy import Integer, MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config.config import pgsql

from dotenv import load_dotenv

load_dotenv()


class Base(DeclarativeBase):
    """Базовый класс.

    Args:
        DeclarativeBase (class): декларативный класс
    """

    metadata = MetaData(schema=pgsql.db_shema)


class User(Base):
    """Модель пользователя.

    Args:
        Base (class): базовый класс
    """

    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tele_id: Mapped[int] = mapped_column(Integer)