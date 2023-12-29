# Використовуємо базовий образ Python
FROM python:3.11.4-slim
LABEL maintainer="katiasimpson17@gmail.com"

COPY requirements.txt requirements.txt


RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN pip install -r requirements.txt pandas sqlalchemy python-dotenv

COPY data_processor.py /usr/src/app/data_processor.py

WORKDIR /usr/src/app
