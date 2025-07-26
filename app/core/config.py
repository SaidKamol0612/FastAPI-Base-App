import logging

from pathlib import Path
from typing import Literal

from pydantic import AmqpDsn
from pydantic import BaseModel
from pydantic import PostgresDsn
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


LOG_DEFAULT_FORMAT = (
    "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
)
CERTIFICATE_DIR = Path(__file__).parent.parent / "certs/"


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000

    # It should be set to False in production
    reload: bool = False


class JWTConfig(BaseModel):
    private_key_path: Path = CERTIFICATE_DIR / "jwt-private.pem"
    public_key_path: Path = CERTIFICATE_DIR / "jwt-public.pem"

    algorithm: str = "RS256"
    expires_minutes: int = 60


class LoggingConfig(BaseModel):
    log_level: Literal[
        "debug",
        "info",
        "warning",
        "error",
        "critical",
    ] = "info"
    log_format: str = LOG_DEFAULT_FORMAT
    log_date_format: str = "%Y-%m-%d %H:%M:%S"

    @property
    def log_level_value(self) -> int:
        return logging.getLevelNamesMapping()[self.log_level.upper()]


class ApiInfo(BaseModel):
    prefix: str = "/api"
    title: str
    description: str
    version: str = "1.0.0"


class DatabaseConfig(BaseModel):
    url: PostgresDsn | str
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    jwt: JWTConfig = JWTConfig()
    run: RunConfig = RunConfig()
    logging: LoggingConfig = LoggingConfig()
    api: ApiInfo
    db: DatabaseConfig


settings = Settings()
