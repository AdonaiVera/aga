FROM python:3.8.6-slim

RUN set eux; \
    apt-get update; \
    apt-get -y upgrade; \
    apt-get install gcc -y; \
    apt-get install g++ -y;

COPY . .

RUN set eux; \
    pip install requests==2.24.0; \
    pip install -r requirements.txt;

EXPOSE 8501
