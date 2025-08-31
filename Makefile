COMPOSE_FILE=docker-compose.yml
DOCKER_COMPOSE=docker compose -f $(COMPOSE_FILE)

.PHONY: up down createsuperuser pytest

# Запуск контейнера
up:
	$(DOCKER_COMPOSE) up -d --build --remove-orphans

# Остановка контейнера
down:
	$(DOCKER_COMPOSE) down

# Создать суперпользователя
createsuperuser:
	$(DOCKER_COMPOSE) exec web python manage.py createsuperuser

pytest:
	$(DOCKER_COMPOSE) exec web pytest
