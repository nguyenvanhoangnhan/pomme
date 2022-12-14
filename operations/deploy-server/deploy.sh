#!/bin/bash

# Pull latest images
cd /root
docker pull psycholog1st/shoe-shop-api
docker pull psycholog1st/shoe-shop-web

# Redeploy applications
docker compose down
docker compose up db web -d
docker compose up api -d

# Initialize api application
docker exec root-api-1 php artisan key:generate
docker exec root-api-1 php artisan config:cache

docker exec root-api-1 php artisan migrate:fresh --seed --force -q

while [[ $? != 0 ]]; do
  docker exec root-api-1 php artisan migrate:fresh --seed --force -q
done


echo "Migration completed"

