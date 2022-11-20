<p align="center">
  <img width="20%" src="./README.assets/granny-smith-logo.svg">
</p>


## What is this?

An e-commerce website that sells shoes, called Pomme.

## What are we using?

Vue 3 w/ Pinia + Django, deploy on DigitalOcean.

<p align="center">
  <img width="88%" src="https://user-images.githubusercontent.com/57064711/202644148-6deae246-92aa-4434-a8b6-b69eeb5bd526.png">
</p>

## Further information:

👉 <a href="https://lucid.app/lucidchart/c0bb1c08-6e3d-44b1-a1e5-bd542c69f643/edit?viewport_loc=47%2C-345%2C3915%2C2152%2C0_0&invitationId=inv_58eb49c0-04af-40dd-a11b-eff68747419a"> Entity Relationship Diagram</a>

## TLDR
```
docker compose up -d 
# API at port 8000
# Web at port 5173
# Postgres DB at port 5432
```

## Installation

```bash
$ cd web && yarn install # client
$ cd api && pip install - requirements.txt # api
```

## Running the app

```bash
# development
$ cd web && yarn dev # client
$ cd api && python3 manage.py runserver 0.0.0.0:8000
```

## Lint

```bash
# eslink
$ cd web && yarn lint
```

## Format code

```bash
# format code
$ cd web && yarn format
```

## Environment variables

```bash
# .env file
API_ROOT=localhost:8000
DATABASE_URL="postgresql://postgres:postgres@localhost:5432/shoeshop"
```

## Databases
Use [PostgreSQL](https://www.postgresql.org/) for our database connection.
Database data is persistent at ./data directory (for local development purpose, don't push them to remote VCS)

```bash
# Please add DB creation, migration commands here
```


Nest is [MIT licensed](LICENSE).
