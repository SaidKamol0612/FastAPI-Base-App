__all__ = (
    "router",
)

from fastapi import APIRouter

from core.config import settings

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

# Include routers of v1