# Instructions

Docs: https://docs.djangoproject.com/en/5.1/

- Create database from your MSSQL. E.g.: test
- Create virtual env: `python -m venv ve`
- Activate virtual env: `ve/Scripts/activate/`
- Install dependecy: `pip install django`
- Create project: `django-admin startproject info`
- Run server: `cd info` y despues `python manage.py runserver`
- Stop program: `CTRL + C`
- Migrate: `python manage.py migrate`

# Create super user

- `python manage.py createsuperuser`
- `python manage.py runserver`
- Search localhost:8000/admin

# Create app

- `python manage.py startapp <app>`

# Migrations of app

- `python manage.py makemigrations`
- `python manage.py migrate`