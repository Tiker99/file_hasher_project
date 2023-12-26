import os
from celery import Celery

environ = os.environ

REDIS_HOST=environ.get('REDIS_HOST')
REDIS_PORT=environ.get('REDIS_PORT')
REDIS_STORE_DB_INDEX=environ.get('REDIS_STORE_DB_INDEX')

RABBITMQ_HOST=environ.get('RABBITMQ_HOST')
RABBITMQ_USERNAME=environ.get('RABBITMQ_USERNAME')
RABBITMQ_PASSWORD=environ.get('RABBITMQ_PASSWORD')
RABBITMQ_PORT=environ.get('RABBITMQ_PORT')


app = Celery(
    'tasks',
    broker=(
        f'pyamqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@'
        f'{RABBITMQ_HOST}:{RABBITMQ_PORT}/'
    ),
    backend=f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_STORE_DB_INDEX}',
    include = ['api.celery_workers.tasks']
)
