# Project Management API

This is a Django-based REST API for managing projects and tasks. It allows users to register, create projects, assign tasks, and manage access control with roles.

## Features

- User authentication with JWT (Admins & Members)
- Admins can create, update, and delete projects & tasks
- Members can only update task statuses
- API endpoints for users, projects, and tasks

## Technologies Used

- Django 5.1.6
- Django REST Framework
- Simple JWT for authentication
- Django Jazzmin for admin panel

Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Create a superuser:
python manage.py createsuperuser

Run the development server:
python manage.py runserver

API Endpoints
Authentication
POST /token/ - Obtain JWT access & refresh tokens
POST /token/refresh/ - Refresh access token
Users
GET /users/ - List all users (Admins only)
POST /users/ - Create a new user
GET /users/{id}/ - Retrieve user details
PUT /users/{id}/ - Update user details
DELETE /users/{id}/ - Delete a user (Admins only)
Projects
GET /projects/ - List all projects
POST /projects/ - Create a project (Admins only)
PUT /projects/{id}/ - Update a project (Only the creator)
DELETE /projects/{id}/ - Delete a project (Only the creator)
Tasks
GET /tasks/ - List all tasks
POST /tasks/ - Create a task (Admins only)
PUT /tasks/{id}/ - Update a task (Admins only, except status update by Members)
DELETE /tasks/{id}/ - Delete a task (Admins only)

Running Tests
Run API tests using:

python manage.py test

