"""Работа с бд."""
import sqlalchemy
from sqlalchemy.orm import Session
from config.config import pgsql as pgsqlsettings
from models.models import Base, User


class PostgresDataBase():
    """Файл для работь с бд."""

    def __init__(self) -> None:
        """Init func."""
        self.dsn = '{driver}://{user}:{password}@{host}:{port}/{name}'.format(
            driver=pgsqlsettings.db_driver,
            name=pgsqlsettings.db_name,
            password=pgsqlsettings.db_password,
            host=pgsqlsettings.db_host,
            port=pgsqlsettings.db_port,
            user=pgsqlsettings.db_user,
        )

        self.engine = sqlalchemy.create_engine(self.dsn)

    def create_all_tables(self) -> bool:
        """Создание таблиц в бд.

        Returns:
            bool: статус выполнения функции.
        """
        try:
            Base.metadata.create_all(self.engine)
        except Exception:
            return False
        return True

    def register_user(self, user_id: int) -> bool:
        user = User(tele_id=user_id)
        with Session(self.engine) as connect:
            connect.add(user)
            connect.commit()
            connect.refresh(user)
        return True

    def get_all_user_ids(self):
        with Session(self.engine) as session:
            try:
                users = session.query(User).all()
                user_ids = [user.tele_id for user in users]
                return user_ids
            finally:
                session.close()


pgsql = PostgresDataBase()
