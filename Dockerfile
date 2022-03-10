FROM python:3.7-slim

WORKDIR /opt/project

COPY requirements.txt .

RUN pip install -r requirements.txt
