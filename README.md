# file_hasher_project
MD5 hash calculation service for files

## Installation

### 1. Configure Environment Variables

Fill in the missing configurations in the `.environment` file located at the root of the project:

# .environment file
RABBITMQ_PASSWORD=
POSTGRES_PASSWORD=

### 2. Then, set the PostgreSQL password in the /docker/postgres/postgres_password file:

# /docker/postgres/postgres_password
your_postgres_password(it must be the same as POSTGRES_PASSWORD in environment file)

### 3. Then, set the rabbitmq default_pass in the /docker/rabbitmq/rabbitmq.conf file:

# /docker/rabbitmq/rabbitmq.conf
default_pass = your_rabbitmq_password(it must be the same as RABBITMQ_PASSWORD in environment file)

### 4. Run the following command to build and start the Docker services:

docker compose up --build -d

### In addition. To add more workers, modify the docker-compose.yml file by appending the following service definition:
worker-{id}:
  container_name: worker-{id}
  build:
    context: .
    dockerfile: docker/celery/Dockerfile
  env_file: ./environment
  environment:
    - WORKER_ID={id}
  volumes:
    - ./api:/usr/src/api/
  depends_on:
    - rabbitmq
    - redis

