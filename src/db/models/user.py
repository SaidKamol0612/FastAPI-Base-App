from datetime import datetime, timezone

from sqlalchemy.orm import Mapped, mapped_column

from ._base import Base


class User(Base):
    id: Mapped[int] = mapped_column(
        nullable=False, primary_key=True, autoincrement=True
    )
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    middle_name: Mapped[str] = mapped_column(nullable=True)
    last_login: Mapped[datetime] = mapped_column(
        nullable=False, default=datetime.now(timezone.utc)
    )
