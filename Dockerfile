FROM python:3.10.12-slim-bullseye

RUN pip3 install --upgrade pip

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install --no-cache-dir -r requirements.txt

RUN pip3 install "uvicorn[standard]" gunicorn
