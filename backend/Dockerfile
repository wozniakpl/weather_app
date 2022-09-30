FROM python:3.9.12-slim-bullseye as base

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  build-essential \ 
  curl \
  python3-psycopg2 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp

RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.2.0
ENV PATH="/root/.local/bin:$PATH"

ADD pyproject.toml /tmp/
ADD poetry.lock /tmp/
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

ENV WAITFORIT_VERSION="v2.4.1"
RUN curl -o /usr/local/bin/waitforit -sSL https://github.com/maxcnunes/waitforit/releases/download/$WAITFORIT_VERSION/waitforit-linux_amd64 && \
  chmod +x /usr/local/bin/waitforit

ADD . /code/

WORKDIR /code/

FROM base as dev

FROM base as dist

ENTRYPOINT [ "docker-entrypoint.sh", "dist" ]
