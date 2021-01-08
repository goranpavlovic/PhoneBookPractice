FROM python:3.9.0-buster

WORKDIR /application

ADD . /application

RUN pip install --upgrade . && python setup.py build

EXPOSE 8080