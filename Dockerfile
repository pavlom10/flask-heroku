FROM python:3-alpine
WORKDIR /app
COPY requirements.txt .
RUN apk update
RUN apk add build-base
RUN apk add postgresql-dev gcc python3-dev musl-dev g++
RUN pip install -r requirements.txt
COPY . .
CMD python run.py