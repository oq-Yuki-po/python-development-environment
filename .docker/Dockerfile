FROM python:3.7.7-slim

RUN apt-get update \
  && apt-get install -y \
  build-essential \
  && pip install poetry

WORKDIR /usr/src

COPY ./ ./

ENV PYTHONPATH="/usr/src:/usr/src/app:$PYTHONPATH"

WORKDIR /usr/src/pip

RUN poetry config virtualenvs.create false \
  && poetry install

WORKDIR /usr/src/app

CMD ["uwsgi","--ini","uwsgi.ini"]