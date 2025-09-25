from fastapi import APIRouter

from core.config import settings


router = APIRouter(
    prefix=settings.api.v1.user_prefix,
    tags=["User"],
)


@router.get("/me")
async def read_user_me() -> dict:
    return {"username": "current_user"}
