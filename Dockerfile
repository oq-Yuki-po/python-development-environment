FROM python:3.7.7-slim

WORKDIR /usr/src

RUN pip install poetry

COPY ./ ./

ENV PYTHONPATH="/usr/src:/usr/src/app:$PYTHONPATH"

RUN poetry config virtualenvs.create false \
  && poetry install