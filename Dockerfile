FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential libssl-dev libffi-dev \
        libopenblas-dev postgresql-client \
        pkg-config && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /findjob_api

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip setuptools wheel &&\
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000