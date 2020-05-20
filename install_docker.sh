#!/bin/bash
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -a -G docker $USER
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose