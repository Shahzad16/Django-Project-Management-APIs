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

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Shahzad16/Django-Project-Management-APIs.git
   cd Django-Project-Management-APIs
    ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```sh
   python manage.py migrate
   ```

5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```sh
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- `POST /users/` - Register a new user
- `POST /token/` - Login user and obtain JWT access & refresh tokens
- `POST /token/refresh/` - Refresh access token

### Users
- `GET /users/` - List all users (Admins only)
- `POST /users/` - Create a new user
- `GET /users/{id}/` - Retrieve user details
- `PUT /users/{id}/` - Update user details
- `DELETE /users/{id}/` - Delete a user (Admins only)

### Projects
- `GET /projects/` - List all projects
- `POST /projects/` - Create a project (Admins only)
- `PUT /projects/{id}/` - Update a project (Only the creator)
- `DELETE /projects/{id}/` - Delete a project (Only the creator)

### Tasks
- `GET /tasks/` - List all tasks
- `POST /tasks/` - Create a task (Admins only)
- `PUT /tasks/{id}/` - Update a task (Admins only, except status update by Members)
- `DELETE /tasks/{id}/` - Delete a task (Admins only)

## Running Tests
Run API tests using:
```sh
python manage.py test
```
