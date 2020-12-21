FROM python:3.7.4-buster

WORKDIR /app

ADD . /app

RUN pip install --upgrade . && python setup.py build

EXPOSE 8080