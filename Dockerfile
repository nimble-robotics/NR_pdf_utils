# FROM ubuntu
FROM python:3.6-stretch
COPY . /app
WORKDIR /app

RUN apt-get update -y
RUN apt-get install python3-pip python3-dev -y
RUN apt-get install build-essential libpoppler-cpp-dev pkg-config -y
RUN apt-get install poppler-utils -y

RUN pip install -r requirements.txt
EXPOSE 5000


CMD python app.py
