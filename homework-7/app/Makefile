# Имя сервисов в docker-compose
DJANGO_SERVICE_NAME = django_app
DB_SERVICE_NAME = postgres_db

# Запуск контейнеров
start:
	docker-compose up -d

# Остановка контейнеров
stop:
	docker-compose down

# Перезагрузка контейнера с Django
restart:
	docker restart $(DJANGO_SERVICE_NAME)

# Перезагрузка контейнера с базой данных
restart-db:
	docker restart $(DB_SERVICE_NAME)

# Создание суперпользователя в Django
createsuperuser:
	docker exec -it $(DJANGO_SERVICE_NAME) python manage.py createsuperuser

# Выполнение миграций в Django
migrate:
	docker exec -it $(DJANGO_SERVICE_NAME) python manage.py migrate

# Применение миграций для приложения core
makemigrations:
	docker exec -it $(DJANGO_SERVICE_NAME) python manage.py makemigrations core

# Сборка образов и запуск
build:
	docker-compose build
	docker-compose up -d

# Очистка и пересоздание контейнеров
rebuild:
	docker-compose down --volumes --remove-orphans
	docker-compose up --build -d

# Получение логов из контейнера с Django
logs:
	docker logs -f $(DJANGO_SERVICE_NAME)

# Получение логов из контейнера базы данных
logs-db:
	docker logs -f $(DB_SERVICE_NAME)

# Очистка и удаление контейнеров
clean:
	docker-compose down --volumes --remove-orphans