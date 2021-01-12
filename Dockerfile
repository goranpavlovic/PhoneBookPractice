FROM python:3.9.0-buster

WORKDIR /application

ADD . /application

ENV PYTHONPATH "$PYTHONPATH:/application"

RUN pip install -e . && python setup.py build

EXPOSE 8080