FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src /app/src

WORKDIR /app/src

CMD ["python", "main.py"]