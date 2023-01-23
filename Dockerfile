FROM python:3.9.15-slim

LABEL MAINTAINER="Jhonatan Matias Martin <jhonatanmatiasmartin@outlook.es>"

WORKDIR /app

RUN apt-get update && rm -r /var/lib/apt/lists/*

RUN mkdir cache && chmod 777 cache 

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD [ "python","main.py"]
