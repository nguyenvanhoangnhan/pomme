<p align="center">
  <img width="20%" src="./README.assets/granny-smith-logo.svg">
</p>


## What is this?

An e-commerce website that sells shoes, called Pomme.

## What are we using?

Vue 3 w/ Pinia + Laravel, deploy on DigitalOcean.

<p align="center">
  <img width="88%" alt="image" src="https://user-images.githubusercontent.com/50044415/206079994-09b92e80-13e9-4c88-ae69-5ed82f740244.png">
</p>

## Further information:

👉 <a href="https://lucid.app/lucidchart/c0bb1c08-6e3d-44b1-a1e5-bd542c69f643/edit?viewport_loc=47%2C-345%2C3915%2C2152%2C0_0&invitationId=inv_58eb49c0-04af-40dd-a11b-eff68747419a"> Entity Relationship Diagram</a>

## TLDR
```
# Start developing
docker compose up db web --build -d
docker compose up api --build -d
# API at port 8000
# Web at port 5173
# MySQL DB at port 3306

# Finish developing
docker compose down # kill all container
```

## Installation

```bash
$ cd web && yarn install # client
$ cd api-laravel && composer install # api
```

## Running the app

```bash
# development
$ cd web && yarn dev # client
$ cd api-laravel && php artisan serve --port=8000 # api
```

## Lint

```bash
$ cd web && yarn lint # web
$ cd api-laravel && vendor/bin/phpcs # api
```

## Format code

```bash
$ cd web && yarn format # web
$ cd api-laravel && vendor/bin/phpcbf # api
```

## Environment variables

```bash
# WEB .env file
VITE_API_URL=http://localhost:8000/api
VITE_CLOUDINARY_URL=https://api.cloudinary.com/v1_1/:cloud_name/
VITE_CLOUDINARY_PRESET=abcxyz


# API .env file
APP_NAME=Laravel
APP_ENV=local
APP_KEY=
APP_DEBUG=true
APP_URL=http://localhost

LOG_CHANNEL=stack
LOG_DEPRECATIONS_CHANNEL=null
LOG_LEVEL=debug

DB_CONNECTION=mysql
DB_HOST=172.17.0.1
DB_PORT=3306
DB_DATABASE=pomme
DB_USERNAME=root
DB_PASSWORD=password123

BROADCAST_DRIVER=log
CACHE_DRIVER=file
FILESYSTEM_DRIVER=local
QUEUE_CONNECTION=sync
SESSION_DRIVER=file
SESSION_LIFETIME=120

JWT_SECRET=lmaolmao
SENTRY_LARAVEL_DSN=
SENTRY_TRACES_SAMPLE_RATE=1.0
SENTRY_ENVIRONMENT=development
```

## Databases
Use MySQL [MySQL](https://www.mysql.com/) for our database connection.

```bash
# Migrate and seed data
cd api-laravel && php artisan migrate:fresh --seed
```


License: [MIT licensed](LICENSE).
