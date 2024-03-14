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

# Проверяем наличие образов без имени
if [ "$(docker images -f "dangling=true" -q)" ]; then
    # Если есть образы без имени, удаляем их
    docker rmi $(docker images -f "dangling=true" -q)
else
    # Если нет образов без имени, выводим сообщение об этом
    echo "No dangling images found."
fi
