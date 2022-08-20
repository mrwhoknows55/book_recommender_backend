FROM python:3.9-slim-buster

RUN mkdir -p /root/app

WORKDIR /root/app
COPY . .
RUN apt update -y && \
 apt install python3-dev cmake gcc libpq-dev -y
RUN pip install -U pip 
RUN pip install -r requirements.txt
