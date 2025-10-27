# Makefile for LekosEPR-API
# Usage examples:
# * make build — install dependencies and apply migrations
# * make run — launch the application
# * make deploy — build and launch from a clean state

.PHONY: migrate build run deploy clean

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
# 3️⃣  Run project
# -----------------------------
run:
	@echo "▶️  Starting LekosEPR-API..."
	PYTHONPATH=src poetry run python -m src.run

# -----------------------------
# 4️⃣  Deploy (build + run)
# -----------------------------
deploy:
	@echo "🚀 Deploying LekosEPR-API..."
	$(MAKE) build
	$(MAKE) run

# -----------------------------
# 5️⃣  Clean temporary files
# -----------------------------
clean:
	@echo "🧹 Cleaning cache and temporary files..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache .mypy_cache dist build
	@echo "✅ Clean complete."
