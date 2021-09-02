From python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt
COPY ./office.csv /app/office.csv

RUN pip install -r requirements.txt

COPY . /app