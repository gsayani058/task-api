# Task API

A Task Management REST API built with Django and Django REST Framework, featuring JWT authentication and per-user data isolation.

## Features

- User registration and login with JWT (access + refresh tokens)
- CRUD operations for tasks (create, list, retrieve, update, delete)
- Users can only view or modify their own tasks (object-level permission check)
- Pagination (5 items per page)
- Filtering tasks by status (`?done=true` / `?done=false`)
- URL-based API versioning (`/api/v1/`)
- Automated tests with pytest covering authentication and authorization

## Tech Stack

Python, Django, Django REST Framework, Simple JWT, SQLite, pytest

## Setup

```bash
git clone https://github.com/gsayani058/task-api.git
cd task-api
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Running Tests

```bash
pytest
```

## API Endpoints

| Method | Endpoint                  | Description                  |
|--------|----------------------------|-------------------------------|
| POST   | `/api/v1/auth/register/`  | Register a new user           |
| POST   | `/api/v1/auth/login/`     | Log in, get access/refresh tokens |
| POST   | `/api/v1/auth/refresh/`   | Refresh an expired access token |
| GET    | `/api/v1/tasks/`          | List your tasks (paginated)   |
| POST   | `/api/v1/tasks/`          | Create a new task             |
| GET    | `/api/v1/tasks/<id>/`     | Retrieve one of your tasks    |
| PUT/PATCH | `/api/v1/tasks/<id>/`  | Update one of your tasks      |
| DELETE | `/api/v1/tasks/<id>/`     | Delete one of your tasks      |

All `/tasks/` endpoints require an `Authorization: Bearer <access_token>` header.

## Security Notes

- Passwords are hashed via Django's `create_user` (never stored in plain text)
- Task ownership is enforced at the queryset level — requesting another user's task returns `404`, not `403`, to avoid confirming the object's existence
- All endpoints require authentication by default (`IsAuthenticated`)