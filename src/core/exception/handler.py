from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette import status

from .exceptions import (
    BadRequestError,
    ForbiddenError,
    NotFoundError,
)


def add_exception_handlers(app: FastAPI):
    def register(exc_class: type[Exception], status_code):
        async def handler(request: Request, exc: type[Exception]):
            return JSONResponse(
                {"detail": str(exc)},
                status_code=status_code,
            )

        app.add_exception_handler(exc_class, handler)

    register(BadRequestError, status.HTTP_400_BAD_REQUEST)
    register(ForbiddenError, status.HTTP_403_FORBIDDEN)
    register(NotFoundError, status.HTTP_404_NOT_FOUND)
