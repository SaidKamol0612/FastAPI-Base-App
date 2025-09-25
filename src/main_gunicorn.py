from core.config import settings
from app import create_app


main_app = create_app(create_custom_static_urls=False)


def guniorn_run():
    """
    Run the application with Gunicorn.
    """

    from core.gunicorn import Application, get_app_options

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
