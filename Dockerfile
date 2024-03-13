FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PTHONUNBUFFERED 1

WORKDIR /usr/src/sight

COPY ./requirements.txt /usr/src/requirements.txt

RUN apt-get update && \
    apt-get upgrade && \
    pip install --upgrade pip && \
    pip install -r /usr/src/requirements.txt

COPY . /urs/src/sight
