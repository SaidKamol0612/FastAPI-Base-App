import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Dict

from fastapi import FastAPI
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.responses import ORJSONResponse
from starlette.responses import HTMLResponse

from api import router as main_router
from core.error import add_exception_handlers
from db import db_helper

log = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # startup
    await db_helper.init_models()

    yield
    # shutdown

    await db_helper.dispose()


def register_static_docs_routes(app: FastAPI) -> None:
    async def custom_swagger_ui_html() -> HTMLResponse:
        return get_swagger_ui_html(
            openapi_url=str(app.openapi_url),
            title=app.title + " - Swagger UI",
            oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
            swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
            swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
        )

    app.add_api_route("/docs", custom_swagger_ui_html, include_in_schema=False)

    async def swagger_ui_redirect() -> HTMLResponse:
        return get_swagger_ui_oauth2_redirect_html()

    app.add_api_route(
        str(app.swagger_ui_oauth2_redirect_url),
        swagger_ui_redirect,
        include_in_schema=False,
    )

    @app.get("/redoc", include_in_schema=False)
    async def redoc_html() -> HTMLResponse:
        return get_redoc_html(
            openapi_url=str(app.openapi_url),
            title=app.title + " - ReDoc",
            redoc_js_url="https://unpkg.com/redoc@next/bundles/redoc.standalone.js",
        )

    app.add_api_route("/redoc", redoc_html, include_in_schema=False)


def config_app(app: FastAPI) -> None:
    add_exception_handlers(app=app)

    async def root() -> Dict[str, str]:
        return {"message": "Hello, World!"}

    app.add_api_route("/", root)
    app.include_router(main_router)


def create_app(
    create_custom_static_urls: bool = False,
) -> FastAPI:
    app = FastAPI(
        default_response_class=ORJSONResponse,
        lifespan=lifespan,
        docs_url=None if create_custom_static_urls else "/docs",
        redoc_url=None if create_custom_static_urls else "/redoc",
    )
    if create_custom_static_urls:
        register_static_docs_routes(app)

    config_app(app)

    return app
