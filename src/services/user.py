from __future__ import annotations
from typing import TYPE_CHECKING, Dict, Any, List, Optional

from core.exception import NotFoundError
from db.repositories import user_repo

if TYPE_CHECKING:
    from db.models import User
    from db.repositories import UserRepo
    from sqlalchemy.ext.asyncio import AsyncSession


class UserService:
    """
    Service for managing User objects.
    """

    def __init__(self, repo: UserRepo):
        self.repo = repo

    async def create_user(
        self,
        *,
        user_data: Dict[str, Any],
        session: AsyncSession,
    ) -> User:
        return await self.repo.create(
            data=user_data,
            session=session,
        )

    async def get_users(
        self,
        *,
        session: AsyncSession,
    ) -> List[User]:
        return await self.repo.get_all(
            session=session,
        )

    async def _get_user_or_raise_error(
        self,
        *,
        user_id: int,
        session: AsyncSession,
    ) -> User:
        user = await self.repo.get_by_id(
            model_id=user_id,
            session=session,
        )
        if not user:
            raise NotFoundError
        return user

    async def get_user(
        self,
        *,
        user_id: int,
        session: AsyncSession,
    ) -> User:
        return await self._get_user_or_raise_error(
            user_id=user_id,
            session=session,
        )

    async def update_user(
        self,
        *,
        user_id: int,
        user_data: Dict[str, Any],
        session: AsyncSession,
    ) -> Optional[User]:
        await self._get_user_or_raise_error(
            user_id=user_id,
            session=session,
        )

        return await self.repo.update(
            model_id=user_id,
            data=user_data,
            session=session,
        )

    async def delete_user(
        self,
        *,
        user_id: int,
        session: AsyncSession,
    ) -> None:
        await self._get_user_or_raise_error(
            user_id=user_id,
            session=session,
        )

        await self.repo.delete(
            model_id=user_id,
            session=session,
        )


user_service = UserService(repo=user_repo)
