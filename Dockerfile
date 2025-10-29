FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o projeto
COPY . .

EXPOSE 3000

# Executa diretamente o seu arquivo principal
CMD ["python", "run.py"]