import sys

from main_gunicorn import guniorn_run
from main_uvicorn import uvicorn_run

def main():
    if sys.platform == "win32":
        # Windows → uvicorn
        uvicorn_run()
    else:
        # Other → gunicorn
        guniorn_run()


if __name__ == "__main__":
    main()
