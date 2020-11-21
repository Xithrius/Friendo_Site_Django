# Friendo_Site
A website for managing Friendo bot and the Friendo API

### start docker
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up

### Deploy
Start the deploy container with:
`docker-compose -f docker-compose.yml -f docker-compose.deploy.yml up -d -build`

Optionally start a dev environment with `sudo docker-compose -p friendo_dev -f docker-compose.yml -f docker-compose.dev.yml up -d --build`

Currently they run on ports 8001 and 8000 respectively.

Point your webserver to these ports with a reverse proxy.