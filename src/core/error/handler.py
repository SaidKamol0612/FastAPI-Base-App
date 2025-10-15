from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from starlette import status

from .errors import (
    BadRequestError,
    ForbiddenError,
    NotFoundError,
)


def add_exception_handlers(app: FastAPI):
    @app.exception_handler(BadRequestError)
    async def bad_request_handler(request: Request, exc: BadRequestError):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": str(exc)},
        )

    @app.exception_handler(ForbiddenError)
    async def forbidden_handler(request: Request, exc: ForbiddenError):
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={"detail": str(exc)},
        )

    @app.exception_handler(NotFoundError)
    async def not_found_handler(request: Request, exc: NotFoundError):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(exc)},
        )
