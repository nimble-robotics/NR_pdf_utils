FROM python:stretch-3.6
COPY . /app
WORKDIR /app

RUN apt-get update -y
RUN apt-get install python3-pip python3-dev -y
RUN apt-get install build-essential libpoppler-cpp-dev pkg-config -y

RUN pip install -r requirements.txt
EXPOSE 5000



CMD python app.py
