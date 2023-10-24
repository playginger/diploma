FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app/posts

COPY ./requirements.txt .

COPY . .

RUN ["python", "manage.py", "migrate"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]