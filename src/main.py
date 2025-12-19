from __future__ import annotations

import uvicorn

from app import create_and_setup_app
from core.config import settings


main_app = create_and_setup_app(create_custom_static_urls=False)


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=settings.run.reload,
    )
