FROM python:3.11.6-slim-bookworm AS builder

RUN apt-get update -y && \
    apt-get install --no-install-recommends -y \
    curl \
    python3-dev \
    libpq-dev \
    gcc \
    netcat-traditional \
    gettext && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv==0.2.2

WORKDIR /usr/src
COPY requirements.txt .

RUN uv pip install --system --cache-dir=/usr/src/.uv_cache -r requirements.txt

FROM python:3.11.6-slim-bookworm

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    UV_CACHE_DIR=/usr/src/.uv_cache

WORKDIR /usr/src

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/src/.uv_cache /usr/src/.uv_cache

RUN apt-get update -y && \
    apt-get install --no-install-recommends -y \
    libpq5 \
    netcat-traditional \
    mc \
    procps && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./app ./app
