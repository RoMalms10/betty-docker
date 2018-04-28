#!/usr/bin/env bash
# Initialization script

git clone https://github.com/eightlimbed/betty-docker.git
cd betty-docker
sudo cp docker-compose.yml /docker-compose.yml
sudo cp betty /usr/bin/
sudo cp pep8 /usr/bin/
sudo cp shellcheck /usr/bin/
sudo docker-compose up -d -f /docker-compose.yml
