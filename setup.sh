#!/usr/bin/env bash
# Initialization script

cp docker-compose.yml /
cp betty /usr/bin/
cp pep8 /usr/bin/
cp shellcheck /usr/bin/
docker-compose -f /docker-compose.yml build
docker-compose -f /docker-compose.yml up -d
