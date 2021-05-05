# syntax = docker/dockerfile:1.2.1
FROM python:3.8
WORKDIR /code 
COPY requirements.txt .
RUN pip3 install -r requirements.txt 
EXPOSE 8000
COPY . /code/
