#!/bin/bash

# Проверяем, запущен ли Docker Compose
if docker-compose ps | grep -q "Up"; then
    echo "Docker Compose is running. Stopping..."
    # Останавливаем Docker Compose
    docker-compose stop
else
    echo "Docker Compose is not running."
fi

# Пересобираем Docker-Compose
docker-compose up --build -d

docker-compose exec web python manage.py migrate

## Удаляем Docker-образ с без имени
docker rmi $(docker images -f "dangling=true" -q)

