FROM python:3.12-slim

WORKDIR /app

COPY consumer/requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY consumer ./consumer
COPY shared ./shared
COPY trustnetai-bert ./trustnetai-bert

WORKDIR /app/consumer

CMD ["python", "consumer.py"]