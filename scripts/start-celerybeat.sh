#!/usr/bin/env bash

cd .. && celery -A core worker -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler