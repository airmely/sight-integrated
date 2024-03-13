#!/bin/bash

# Запуск celery
cd .. && celery -A core flower --port=5555 -l INFO
