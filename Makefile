.PHONY: build run

build:
	@echo "Building FastSimpleCRM..."
	poetry env activate
	poetry install
	@echo "Build complete."

run:
	@echo "Running FastSimpleCRM..."
	poetry run start