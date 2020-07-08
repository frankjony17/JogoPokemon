FROM postgres:latest
ENV POSTGRES_PASSWORD="Mo680A94dS2RvHmUDA8Y"
ADD pokemon.sh /
RUN cat /pokemon.sh >> /docker-entrypoint-initdb.d/postgis.sh

