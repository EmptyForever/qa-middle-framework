FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY mock_api/ ./mock_api/
COPY src/ ./src/

ENV PYTHONPATH=/app

CMD ["uvicorn", "mock_api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
