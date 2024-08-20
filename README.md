# Order Processing System

## Описание

Система для обработки заказов с использованием FastAPI, RabbitMQ и PostgreSQL.

## Как запустить проект

1. Склонируйте репозиторий
2. Установите зависимости: "pip install -r requirements.txt"
3. Создайте и примените миграции баз данных
4. Запустите приложение: "uvicorn app.main:app --reload"
5. Запустите consumers: "python app/consumers/prder_consumer.py" и "python app/consumers/notification_consumer.py"

## Как выполнить миграции базы данных

1. Установите Alembic: "pip install alembic"
2. Создайте миграцию: "alembic revision --autogenerate -m 'Initial migration'"
3. Примените миграцию: "alembic upgrade head"

# Как запустить тесты

1. Установите pytest: "pip install pytest"
2. Запустите тесты: "pytest"

## Как работать с очередями RabbitMQ

1. Убедитесь, что RabbitMQ запущен
2. Создайте очереди:
    - "order_processing" для обработки заказов
    - "notification" для отправки уведомлений