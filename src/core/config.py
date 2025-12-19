from __future__ import annotations

import logging
import multiprocessing
from pathlib import Path
from typing import Literal, Optional

from pydantic import BaseModel, Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

# =========================
# Paths
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db.sqlite3"
LOGS_DIR = BASE_DIR / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)


# =========================
# Logging defaults
# =========================
LOG_DEFAULT_FORMAT = (
    "[%(asctime)s.%(msecs)03d] "
    "%(module)16s:%(lineno)-3d "
    "%(levelname)-8s - %(message)s"
)
LOG_DEFAULT_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class ApiPrefixSettings(BaseModel):
    class ApiV1Prefix(BaseModel):
        prefix: str = "/v1"
        users_prefix: str = "/users"

    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class DatabaseSettings(BaseModel):
    class DBURLSetting(BaseModel):
        db_type: str = "sqlite"
        db_driver: str = "aiosqlite"
        db_user: Optional[str] = "user"
        db_pass: Optional[str] = "password"
        db_host: Optional[str] = "localhost"
        db_port: Optional[int] = 5432
        db_name: Optional[str] = "mydb"
        db_path: Optional[Path] = DB_PATH  # for SQLite

        @field_validator("db_path", mode="before")
        def check_required_fields(cls, v, info):
            values = info.data
            db_type = values.get("db_type", "sqlite")
            if db_type == "sqlite" and not v:
                raise ValueError("db_path is required for SQLite")
            return v

        @property
        def resolved_url(self) -> str:
            if self.db_type == "sqlite":
                return f"{self.db_type}+{self.db_driver}:///{self.db_path}"
            else:
                if not all(
                    [
                        self.db_user,
                        self.db_pass,
                        self.db_host,
                        self.db_port,
                        self.db_name,
                    ]
                ):
                    raise ValueError("Missing required DB connection info")
                return f"{self.db_type}+{self.db_driver}://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"

    url: DBURLSetting = Field(default_factory=DBURLSetting)
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10
    pool_pre_ping: bool = True

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class GunicornSettings(BaseModel):
    workers: Optional[int] = None
    timeout: int = 900
    keepalive: int = 5
    preload_app: bool = False

    @property
    def resolved_workers(self) -> int:
        return self.workers or (multiprocessing.cpu_count() * 2 + 1)


class LoggingSettings(BaseModel):
    level: Literal[
        "debug",
        "info",
        "warning",
        "error",
        "critical",
    ] = "info"

    format: str = LOG_DEFAULT_FORMAT
    date_format: str = LOG_DEFAULT_DATE_FORMAT

    access: bool = True
    file_enabled: bool = False
    file_path: Path = LOGS_DIR / "app.log"

    @property
    def level_value(self) -> int:
        return getattr(logging, self.level.upper(), logging.INFO)


class RunSettings(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000

    debug: bool = False
    reload: bool = False


# =========================
# Root settings
# =========================
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_prefix="CONFIG__",
        env_file=BASE_DIR / ".env",
        env_nested_delimiter="__",
    )

    api: ApiPrefixSettings = Field(default_factory=ApiPrefixSettings)
    db: DatabaseSettings = Field(default_factory=DatabaseSettings)
    gunicorn: GunicornSettings = Field(default_factory=GunicornSettings)
    logging: LoggingSettings = Field(default_factory=LoggingSettings)
    run: RunSettings = Field(default_factory=RunSettings)


settings = Settings()
