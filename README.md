# IPP Dealership

This is a full stack web application for a car/motorcycle dealership. It is built using Django and Django REST Framework.

It's a work in progress and more features will be added in the future. The main goal of this project is to learn Django and Django REST Framework. The project was proposed by professor [João Ventura](https://github.com/joaoventura) from the Instituto Politécnico de Portalegre.

## Table of Contents

- [Technologies](#technologies)
- [Features](#features)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)

## Technologies

- Django
- Django REST Framework
- SQLite
- HTML
- CSS (Bootstrap)
- JavaScript

## Features

- User authentication
- CRUD operations for vehicles
- Rest API for vehicles
- Search functionality
- Pagination

## Installation

1. Clone the repository
2. Create a virtual environment with the command `python -m venv .venv`
3. Activate the virtual environment with the command `source .venv/bin/activate` on Linux or `.venv\Scripts\activate` on Windows
4. Install the dependencies with the command `pip install -r requirements.txt`
5. Run the migrations with the command `python manage.py migrate`
6. Create a superuser with the command `python manage.py createsuperuser`
7. Run the server with the command `python manage.py runserver`

## API Endpoints

- `/api/v1/auth/token/` - POST - Obtain a token
- `/api/v1/auth/token/refresh/` - POST - Refresh a token
- `/api/v1/auth/token/verify/` - POST - Verify a token
- `/api/v1/cars/` - GET, POST - List all cars or create a new car.
- `/api/v1/cars/<int:pk>/` - GET, PUT, DELETE - Retrieve, update or delete a car.
- `/api/v1/motorcycles/` - GET, POST - List all motorcycles or create a new motorcycle.
- `/api/v1/motorcycles/<int:pk>/` - GET, PUT, DELETE - Retrieve, update or delete a motorcycle.

## Screenshots

![Home](https://imgur.com/eYMRZEB.png)
![Motorcycles](https://imgur.com/nfhLLJ4.png)
![API Token](https://imgur.com/4t3COKi.png)

## License

This project is licensed under the terms of the MIT license. For more details, see the [LICENSE](LICENSE) file.
