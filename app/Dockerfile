FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /code

COPY requirements.txt /code/
COPY ./entrypoint.sh /code/app/entrypoint.sh

RUN pip install -r requirements.txt
RUN apt update
RUN apt install -y netcat

COPY . /code/

ENTRYPOINT ["/bin/bash", "/code/entrypoint.sh"]