FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Dummy values for collectstatic - real values provided at runtime
RUN SECRET_KEY=build-only-dummy-key \
    DEBUG_STATE=False \
    DND_PASSWORD=x \
    VAMPIRE_PASSWORD=x \
    KULT_PASSWORD=x \
    DAGGERHEART_PASSWORD=x \
    python3 manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "codexumbrae.wsgi:application"]
