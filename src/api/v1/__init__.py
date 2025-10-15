__all__ = ("router",)

from fastapi import APIRouter

from core.config import settings

from .views import router as views_router

router = APIRouter(prefix=settings.api.v1.prefix)
router.include_router(views_router)
