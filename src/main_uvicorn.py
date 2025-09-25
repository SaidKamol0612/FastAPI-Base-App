import logging
import uvicorn

from core.config import settings
from app import create_app


logging.basicConfig(
    filename=settings.logging.log_file if not settings.run.debug else None,
    level=settings.logging.log_level_value,
    datefmt=settings.logging.date_format,
    format=settings.logging.log_format,
)

main_app = create_app(create_custom_static_urls=False)


def uvicorn_run():
    """
    Run the application with Uvicorn.
    """

    uvicorn.run(
        "main_uvicorn:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=settings.run.reload,
    )


if __name__ == "__main__":
    uvicorn_run()
