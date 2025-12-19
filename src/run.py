from __future__ import annotations

from core import settings
from core.gunicorn import get_app_options, Application
from main import main_app


def run_gunicorn():
    """
    Run FastAPI app with Gunicorn.
    """

    options = get_app_options(
        host=settings.run.host,
        port=settings.run.port,
        timeout=settings.gunicorn.timeout,
        workers=settings.gunicorn.resolved_workers,
        log_level=settings.logging.level,
    )

    Application(main_app, options).run()


if __name__ == "__main__":
    run_gunicorn()
