#!/bin/bash

# Запуск celery
cd .. && celery -A core worker -l INFO
