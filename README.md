# Python-Backend-Course
Repository with all materials for the Python-Backend Course (HSE SE 2 year)

## Homework 5
Currently implemented:
- Django app ([/app folder](./homework-5/app/app))
- Docker file with Docker configuration ([Dockerfile](./homework-5/app/Dockerfile))
- Docker-compose file with PostgreSQL database and Django App startup configuration ([docker-compose.yml](./homework-5/app/docker-compose.yml))
- Makefile with commands for running the app ([Makefile](./homework-5/app/Makefile))
- Basic API endpoints for User, Post and Comment models (`/api/users/`, `/api/posts/`, `/api/comments/`)
- Basic CRUD operations for User, Post and Comment models (`/api/users/{id}/`, etc.)
- Like (and unlike) features for Posts and Comments (`/api/posts/{id}/like/`, `/api/comments/{id}/unlike/`, etc.)
- Default authentication with User model
- Default Swagger documentation for all available endpoints (`/swagger/`)

### Makefile

For testing the app locally, you can use the following commands:

0. Create `.env` file with database credentials and Django secret key (see [.env.example](./homework-5/app/.env.example))
1. Run `make build` to build the Docker image
2. Run `make migrate` to apply migrations
3. Run `make restart` to restart the Docker container with Django App (to apply migrations)
4. Run `make createsuperuser` to create a superuser for administrating the app
5. Go to `http://localhost:8000/swagger/` to see Swagger documentation **_or_**
6. Go to `http://localhost:8000/api/` to see all API endpoints and work with them through Django Rest Framework

**Note:** The app is in development mode, so `DEBUG=True` is set in the [settings.py](./homework-5/app/app/settings.py) file.

**Note:** Makefile was written for Windows 11, so its workability is not guaranteed for MacOS and Linux. Please make sure to use proper commands, especially related to Python virtual environment.