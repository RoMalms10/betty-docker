#!/usr/bin/env bash
# Initialization script

sudo cp docker-compose.yml /docker-compose.yml
cd / && sudo docker-compose up -d
sudo cp betty /usr/bin/
sudo cp pep8 /usr/bin/
sudo cp shellcheck /usr/bin/
