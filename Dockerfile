FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PTHONUNBUFFERED 1

WORKDIR /usr/src/sight

COPY ./requirements.txt /usr/src/requirements.txt

RUN apt-get update && \
    apt-get upgrade && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN python -m venv venv

COPY . /urs/src/sight
