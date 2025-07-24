# CHANGES.md

## 📅 [2025-07-24] – Full Refactor and JWT Integration by K Jaswanth

---

### 🚨 Initial Issues Identified

- Code was entirely monolithic (`app.py` handled everything)
- No input validation or error handling
- Hardcoded secrets (DB paths, passwords)
- No authentication/login endpoint
- No modular separation for routes, models, services
- Circular imports due to tight coupling

---

### ✅ Refactoring & Restructuring

- Introduced **Flask app factory pattern** (`create_app()` in `__init__.py`)
- Added clear folders: `models/`, `routes/`, `services/`, `schemas/`, `utils/`
- Split business logic (`user_service.py`) and routes (`user_routes.py`)
- Created proper validation using **Marshmallow**
- Added centralized error handling in `error_handlers.py`
- Used `.env` and `config.py` for secret and database config
- Created reusable project structure with clean `requirements.txt`

---

### 🔐 Security & Authentication

- Added **JWT-based login** at `POST /login`
- Stored passwords as hashed values using `werkzeug.security`
- Introduced `auth_service.py` for login + token generation
- Tokens expire after 1 hour and use a secret from `JWT_SECRET_KEY`

---

### 🧪 Testing

- Added basic `pytest` test suite for `/users` CRUD operations
- Tests run against in-memory SQLite DB
- Validates structure, status codes, and DB updates

---

### 📝 Documentation

- Updated `README.md` with:
  - Setup, installation, and API usage
  - Endpoint list including `/login`
  - Environment variables and DB instructions
- Created this `CHANGES.md` to track improvements

---

### 🤖 AI Usage Transparency

- Used ChatGPT for:
  - Initial prompts for modular Flask app
  - JWT integration scaffolding
  - Circular import resolution strategy
  - README and CHANGES.md drafting
- All AI output was reviewed and hand-edited before final use

---

### 🧩 Future Recommendations

- Add unit tests for `/login` and protected routes
- Add decorators for token-protected endpoints
- Use Flask-Migrate for schema migrations
- Replace SQLite with PostgreSQL for production
