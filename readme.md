# Secure REST API with Django REST Framework

## Overview

This project is a REST API built with Django REST Framework.
The goal is to design a system for tracking technical issues, including projects, contributors, tickets, and comments, with a role-based permission system.

The project was completed as part of the OpenClassrooms Python Developer program.

## Features

- CRUD operations for projects, issues, and comments
- JWT authentication
- Role-based permissions
- API testing with Postman

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- Postman

## Installation

### Clone the Repository

- `git clone https://github.com/fabroyer/django-rest-api.git`
- `cd django-rest-api`

### Create and Activate Virtual Environment

Windows:
```bash
python -m venv env
env\Scripts\activate
```

Mac/Linux:
```bash
python -m venv env
source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Run the Development Server

```bash
python manage.py runserver
```

Open in browser:

http://127.0.0.1:8000/admin/

### Default Credentials

- Username: admin
- Password: admin

## API Documentation (Postman)

- Postman URL: `https://documenter.getpostman.com/view/31593605/2sA2xcZZsF`

## Application Overview

This API provides a technical issue tracking system that allows users to manage projects, contributors, tickets, and comments.
It implements a role-based permission system to control access and actions.