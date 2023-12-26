#!/bin/bash

psql --username postgres <<-EOSQL
    CREATE DATABASE "boston";
    CREATE USER boston WITH PASSWORD '$POSTGRES_PASSWORD';
    GRANT ALL PRIVILEGES ON DATABASE boston to boston;
EOSQL

psql --username postgres --dbname boston <<-EOSQL
    GRANT ALL ON SCHEMA public TO boston;
EOSQL

psql -U boston -d boston -f /tmp/init.sql