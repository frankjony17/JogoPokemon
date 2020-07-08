#!/bin/sh

set -e

# Perform all actions as $POSTGRES_USER
export PGUSER="postgres"

# Create the 'template_postgis' template db
psql <<- 'EOSQL'
CREATE DATABASE pokemon_db;
EOSQL

psql --dbname="pokemon_db" <<- 'EOSQL'
CREATE ROLE pokemon LOGIN SUPERUSER PASSWORD 'pokemon.123';
EOSQL
