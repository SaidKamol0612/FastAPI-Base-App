__all__ = ("router",)

from fastapi import APIRouter

from core.config import settings

from .user import router as user_router

router = APIRouter(prefix=settings.api.v1.prefix)
router.include_router(user_router)
