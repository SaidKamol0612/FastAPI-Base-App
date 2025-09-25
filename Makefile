.PHONY: build run

build:
	@echo "FastAPI-Base-App..."
	poetry env activate
	poetry install
	@echo "Build complete."

run:
	@echo "Running FastAPI-Base-App..."
	poetry run start