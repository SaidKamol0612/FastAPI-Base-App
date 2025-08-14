__all__ = ("router",)

from fastapi import APIRouter

from core.config import settings

from .v1 import router as v1_router

router = APIRouter()

# Include routers of api
router.include_router(v1_router)
