# TODO CRUD API

This is a simple Django Rest Framework-based project that provides a RESTful API for managing TODO tasks. The API supports full CRUD (Create, Read, Update, Delete) functionality.

## Features
- Create TODOs with fields:
  - `title` (string)
  - `description` (text, optional)
  - `due_date` (datetime)
  - `is_completed` (boolean, default: false)
- View, Update, and Delete TODOs.

## Endpoints
The API exposes the following endpoints under `/api/todos/`:
- `GET /api/todos/` - List all TODOs.
- `POST /api/todos/` - Create a new TODO.
- `GET /api/todos/<id>/` - Retrieve a TODO by its ID.
- `PUT /api/todos/<id>/` - Update a TODO.
- `DELETE /api/todos/<id>/` - Delete a TODO.

## Installation
1. Clone the repository:
   ```bash
   git clone <GitHub_repository_URL>
   cd todo_project

## Technologies
- Python
- Django
- Django Rest Framework

