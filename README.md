# Проект «Фудграм»

## Автор

Дмитрий «Maitzen» Войтов

## Описание

«Фудграм» — web-приложение, позволяющее пользователям публиковать рецепты блюд,
подписываться на публикации других пользователей (авторов рецептов), добавлять
понравившиеся рецепты в список избранного, а также загружать на своё устройство
список продуктов, необходимых для приготовления одного или нескольких выбранных
блюд, что особенно удобно делать перед походом в супермаркет.

## Ключевые функции

- Регистрация и авторизация пользователей
- Создание и просмотр, редактирование и удаление рецептов
- Подписка на других пользователей (авторов рецептов)
- Добавление рецептов в список избранного и список покупок
- Загрузка списка покупок на устройство пользователя

## Стек

### Frontend
- JavaScript
- Nginx
- React 17.0.1
- React Router DOM

### Backend
- Docker
- Docker Compose
- Django
- Django REST Framework
- PostgreSQL
- Python 3.9.13

## Установка и запуск

### Требования
- Docker
- Docker Compose

### Пошаговая инструкция

1. Склонируйте репозиторий и перейдите в каталог проекта,
выполнив следующие команды:
```bash
git clone git@github.com:maitzen/foodgram-st.git
cd foodgram-st
```

2. Создайте `.env`-файл (например, `example.env`)
в каталоге backend и наполните его следующим содержимым:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
DEBUG=False
ALLOWED_HOSTS=127.0.0.1,localhost
```

3. Перейдите в каталог frontend и выполните следующие команды:
```bash
npm install --legacy-peer-deps
npm run build
```

4. Перейдите в каталог infra и запустите проект
с пересборкой посредством Docker Compose:
```bash
docker-compose up -d --build
```

5. Выполните загрузку ингредиентов в базу данных:
```bash
docker-compose exec backend python manage.py load_ingredients
```
