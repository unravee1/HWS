FROM python:3.10

COPY main.py /app/main.py

RUN apt-get update && apt-get install -y iputils-ping

WORKDIR /app

CMD python3 main.py