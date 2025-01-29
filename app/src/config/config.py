"""Файл конфигураций."""
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class BaseServisSettings(BaseSettings):
    """Настройки сервиса.

    Args:
        BaseSettings (class): базовые настройки.
    """

    model_config = SettingsConfigDict(
        env_file='.env.example',
        extra='ignore',
    )


class PgSqlSettingsq(BaseServisSettings):
    """Валидация данных для PostgreSQL.

    Args:
        BaseServisSettings (class): Настройки сервиса.
    """

    db_host: str
    db_password: str
    db_port: int
    db_shema: str
    db_name: str
    db_user: str
    db_driver: str


class Telegram(BaseServisSettings):
    """Валидация данных для телеграмма.

    Args:
        BaseServisSettings (class): Настройки сервиса.
    """
    token: str
    admin_id: str


tgsettings = Telegram()
pgsql = PgSqlSettingsq()
