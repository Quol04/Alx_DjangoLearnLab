# LibraryProject

A simple Django-based Library Project used for learning and demonstration purposes. This repository contains a minimal Django application showing the standard project layout, basic configuration, and instructions to run and test the app locally.

---

## Table of contents

- Project overview
- Prerequisites
- Installation
- Running the project (development)
- Database migrations & superuser
- Testing
- Project structure
- Deployment notes

---

## Project overview

`LibraryProject` is a beginner-friendly Django project included as part of a hands-on learning course. It demonstrates a typical Django setup with the project package, a SQLite database for local development, and guidance for common developer workflows (migrations, creating a superuser, running the dev server).

This repository is intentionally small and focused on the essentials needed to learn Django project structure and commands.

---

## Prerequisites

- Python 3.8+ (3.10 or later recommended)
- pip (or pipenv/virtualenv) for managing Python packages
- (Optional) virtual environment tool such as `venv` or `virtualenv`

Note: This README shows commands that work in Windows PowerShell (the user's default shell). Adjust slightly for other shells (bash, zsh) if needed.

---

## Installation

1. Open a PowerShell terminal and change directory into the project root (the folder that contains `manage.py`):

   cd "c:\Users\Lenovo\Desktop\Alx-Software-Eng\Backend Program\9-week-nine-django\Alx_DjangoLearnLab\Introduction_to_Django\LibraryProject"

2. (Recommended) Create and activate a virtual environment:

   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

3. Install dependencies. If a `requirements.txt` file exists, run:

   pip install -r requirements.txt

   If there is no `requirements.txt`, install Django directly for a minimal setup:

   pip install django

---

## Running the project (development)

1. Apply migrations:

   python manage.py migrate

2. Create a superuser (follow prompts):

   python manage.py createsuperuser

3. Run the development server:

   python manage.py runserver

4. Open your browser and visit:

   http://127.0.0.1:8000/

   The admin site will be available at `http://127.0.0.1:8000/admin/` once a superuser has been created.

---

## Database migrations & superuser

- To generate migration files after model changes:

  python manage.py makemigrations

- Apply migrations to update the database schema:

  python manage.py migrate

- Create or manage the admin user:

  python manage.py createsuperuser

---

## Testing

If the project contains tests, run them with:

python manage.py test

If no tests exist, consider adding basic unit tests for models and views as a learning exercise.

---

## Project structure

At a glance (top-level files and directories):

- `manage.py` - Django's command-line utility for administrative tasks
- `db.sqlite3` - SQLite database file (committed here for convenience; consider excluding in production)
- `LibraryProject/` - Django project package containing settings, URLs, WSGI/ASGI entry points

Inside `LibraryProject/` (project package):

- `__init__.py`
- `settings.py` - Django settings
- `urls.py` - URL declarations
- `wsgi.py` / `asgi.py` - WSGI/ASGI entry points

If you add apps to the project, they will live alongside these files (e.g., `books/`, `catalog/`, etc.).

---

## Environment & configuration

- This project uses the default settings in `LibraryProject/settings.py`. For production, verify and secure the following:

  - SECRET_KEY must be kept secret (do not commit an insecure key)
  - DEBUG must be set to `False` in production
  - ALLOWED_HOSTS should include your domain(s)

- Consider using environment variables (via `python-decouple`, `django-environ`, or OS env vars) to manage secrets and environment-specific settings.



<!-- =============== -->
# Django Permissions & Groups Setup

## Custom Permissions
The `bookshelf` model defines the following permissions:

- `can_view`
- `can_create`
- `can_edit`
- `can_delete`

These are used to control access to bookshelf views.

## Groups
Three groups are created:

### Viewers
- can_view

### Editors
- can_view
- can_create
- can_edit

### Admins
- can_view
- can_create
- can_edit
- can_delete

## Enforcing Permissions in Views
Views use Django's `permission_required` decorator, for example:

```python
@permission_required('bookshelf.can_edit', raise_exception=True)
def article_edit(request, pk):
    ...
