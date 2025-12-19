.PHONY: migrate build run deploy clean


APP_TITLE="FastAPI-Base-App by SaidKamol0612."

# -----------------------------
# 1️⃣  Migrations
# -----------------------------
migrate:
	@echo "🚀 Running database migrations..."
	cd src && poetry run alembic upgrade head

# -----------------------------
# 2️⃣  Building application
# -----------------------------
build:
	@echo "📦 Installing dependencies..."
	poetry install
	$(MAKE) migrate
	@echo "✅ Build complete."

# -----------------------------
# 3️⃣.1  Run app via Uvicorn
# -----------------------------
uvicorn_run:
	@echo "Running ${APP_TITLE} via Uvicorn..."
	PYTHONPATH=src poetry run python -m src.main

# -----------------------------
# 3️⃣.2 Run app via Gunicorn
# -----------------------------
gunicorn_run:
	@echo "Running ${APP_TITLE} via Gunicorn..."
	PYTHONPATH=src poetry run python -m src.run

# -----------------------------
# 5️⃣  Clean temporary files
# -----------------------------
clean:
	@echo "🧹 Cleaning cache and temporary files..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache .mypy_cache dist build
	@echo "✅ Clean complete."
