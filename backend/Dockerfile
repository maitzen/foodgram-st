# Для сборки контейнера используется образ Python версии 3.9.13
FROM python:3.9.13

# Назначение рабочего каталога
WORKDIR /app

# Установка зависимостей

# Копирование перечня зависимостей в рабочий каталог внутри контейнера
COPY requirements.txt .

# Установка всех зависимостей из перечня без сохранения кэша pip
RUN pip install --no-cache-dir -r requirements.txt


# Копирование проекта
COPY . .

# Создание каталога для статических файлов
RUN mkdir -p /app/static/

# Запуск миграций, сбор статики и запуск сервера
CMD sh -c "python manage.py collectstatic --noinput && \
           python manage.py migrate && \
           gunicorn foodgram.wsgi --bind 0.0.0.0:8000"
