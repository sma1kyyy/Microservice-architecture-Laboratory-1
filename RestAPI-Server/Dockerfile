FROM python:3.13.2-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080
CMD ["sh", "-c", "pwd && uvicorn cmd.main:app --host 0.0.0.0 --port 8080"]