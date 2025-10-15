.PHONY: build run

build:
	@echo "Building FastAPIBaseApp..."
	poetry install
	@echo "Build complete."

run:
	@echo "Running FastAPIBaseApp..."
	cd src && poetry run python run.py