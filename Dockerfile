FROM python:3.12-slim


RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ../requirements.txt /app/

RUN pip install --no-cache-dir -r /Users/vladhramenko/PycharmProjects/BackWSKA/DRF-1-course-project/ShopApi/requirements.txt

COPY ShopApi /app/

EXPOSE 8000 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
