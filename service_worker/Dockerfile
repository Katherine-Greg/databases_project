# Використовуємо базовий образ Python
FROM python:3.11.4-slim
LABEL maintainer="katiasimpson17@gmail.com"

COPY requirements.txt requirements.txt


RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN pip install -r requirements.txt django-crispy-forms python-dotenv

COPY main.py /usr/src/app/main.py

WORKDIR /usr/src/app
