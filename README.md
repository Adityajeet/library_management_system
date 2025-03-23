# Library Management System using Django

## Project Overview
This is a Django-based Library Management System that allows admins to perform CRUD operations on books and provides a student view to list all books.

## Features
- **Admin Operations**:
  - Signup: Create a new admin account.
  - Login: Allow admin login using email and password.
  - Book Management: Create, read, update, and delete books.
- **Student View**:
  - List all books.

## Setup Instructions

### Prerequisites
- Python 3.8+
- MySQL
- Django 5.1.7
- Django REST Framework
- `mysqlclient` (Python MySQL adapter)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Adityajeet/library_management_system.git

2. Create a virtual environment and Install requirements.txt
    ```bash
    pip install -r requirements.txt

3. Configure the database in settings.py (library_management\library_management\settings.py) as
   ```bash
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library_db',
        'USER': 'root',
        'PASSWORD': 'pass',  #write your password. the password written in the is mine one.
        'HOST': 'localhost',
        'PORT': '3306',
    }}

4. Open Mysql and create a database
   ```bash
   CREATE DATABASE library_db;

5. Run migration and start the server
   ```bash
   cd library_management
   python manage.py migrate
   python manage.py runserver

6. API Endpoints
Admin Signup: POST:  http://127.0.0.1:8000/api/signup/

Admin Login: POST: http://127.0.0.1:8000/api/token/

Book List/Create: GET/POST: http://127.0.0.1:8000/api/books/

Book Retrieve/Update/Delete: GET/PUT/DELETE: http://127.0.0.1:8000/api/books/<id>/

Student Book List: GET http://127.0.0.1:8000:/api/student/books/
