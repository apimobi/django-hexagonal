FROM python:3.11.6-slim as base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    libpq-dev \
    python3-dev \
    ; \
    rm -rf /var/lib/apt/lists/*

RUN pip install poetry==1.7.1
RUN poetry config virtualenvs.create false

WORKDIR /app

COPY pyproject.toml poetry.lock ./


FROM base as dev

RUN poetry install --no-interaction --no-ansi

COPY . .


CMD ["hexa/manage.py", "runserver", "0.0.0.0:8080"]

