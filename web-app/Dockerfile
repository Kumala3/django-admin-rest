FROM python:3.11-slim

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install -r /usr/src/app/requirements.txt

COPY . /usr/src/app
