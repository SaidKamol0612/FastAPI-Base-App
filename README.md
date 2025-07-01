# ⚒️ FastAPI Base App

This basic FastAPI application serves as a starter template for building web services and APIs. It includes a minimal project structure with clear separation of routes, models, and configuration. The template supports asynchronous requests, data validation with Pydantic, and automatic OpenAPI documentation. It also provides the foundation for integrating a database and using dependency injection. Designed for easy scalability, this template is suitable for both learning and production-ready development.

---

## 🧰 Libraries and Tools

- FastAPI — Web framework for building APIs.
- SQLAlchemy — SQL ORM for database access.
- Alembic — Lightweight database migration tool.
- Uvicorn — ASGI server to run FastAPI.

---

## 🚀 Quick Start

1. **Clone the repository:**

   ```bash
   git clone https://github.com/SaidKamol0612/Online-Store-API.git
   ```

2. **Create and activate `venv`:**

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables to `env` file:**

   ```bash
   APP_CONFIG__RUN__RELOAD=1

   APP_CONFIG__API__TITLE="FastAPI Base App"
   APP_CONFIG__API__DESCRIPTION="Base site API on FastAPI"

   APP_CONFIG__DB__URL="postgresql+asyncpg://user:pwd@localhost:5432/app"
   APP_CONFIG__DB__ECHO=1
   ```

5. **Run the server:**

   ```bash
   cd app
   python run.py
   ```

6. **Open in browser:**

   - Home page: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔓 License and Contribution

This project is open and free to extend. You may use it in commercial or personal projects with minimal restrictions. Attribution is appreciated but not required.

> 💡 Contributions and forks are welcome!
