import sys
import uvicorn

from core.config import settings
from main_uvicorn import main_app


def guniorn_run():
    from core.gunicorn import Application, get_app_options

    # Other → gunicorn
    Application(
        application=main_app,
        options=get_app_options(
            host=settings.gunicorn.host,
            port=settings.gunicorn.port,
            timeout=settings.gunicorn.timeout,
            workers=settings.gunicorn.workers,
            log_level=settings.logging.log_level,
        ),
    ).run()


if __name__ == "__main__":
    guniorn_run()
