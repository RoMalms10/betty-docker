#!/usr/bin/env bash
# Initialization script

docker-compose build
docker-compose up -d
sudo cp betty /usr/bin/
sudo cp pep8 /usr/bin/
sudo cp shellcheck /usr/bin/
