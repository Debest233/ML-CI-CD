FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Jeśli masz aplikację FastAPI, uruchomi się to. Jeśli nie, kontener po prostu się zbuduje.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]