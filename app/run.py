import uvicorn

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.responses import ORJSONResponse

from core import settings
from core.db import db_helper
from utils import templates


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # startup

    yield
    # shutdown
    await db_helper.dispose()


app = FastAPI(
    title=settings.api.title,
    description=settings.api.description,
    version=settings.api.version,
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": settings.api.title,
            "author": "Mirsaidov Saidkamol",
        },
    )


if __name__ == "__main__":
    uvicorn.run(
        "run:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=settings.run.reload,
    )
