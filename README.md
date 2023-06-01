# Lisci task
Mini Django app with Django-Rest-Framework and Graphene-Django created for Lisci.

## Dependendencies
- `python3.11`
- `django` + `django rest framework` + `graphene-django` -> Used for developments of the BE Application, Graphql and REST API.
- all other dependencies can be found in `requirements.txt`

## How to use
### Docker Environment
- As a part of the projects, there is a Dockerfile and docker-compose.yaml, so that the app can be run without 
need to setup the local environment. 
- Only necessary things to be install is [Docker](https://docs.docker.com/engine/install/).
- Then just navigate to the top folder and run:
```bash
docker-compose up --build
```
### Local Environment
#### PostgreSQL Setup
- Install PostgreSQL 
- Creating the PostgreSQL Database and User
```bash
1. CREATE DATABASE lisci;
2. CREATE USER lisci WITH PASSWORD='lisci';
3. GRANT ALL PRIVILEGES ON DATABASE lisci TO lisci;
```
#### Django Setup
- Create a virtual environment and activate it
```bash
python3 -m venv venv
source /venv/bin/activate
```
- Install all necessary libraries
```bash
python3 -m pip install -r requirements.txt 
```
- Migrate the database (make sure you are in the `LisciTask` folder)
```bash
python3 manage.py migrate 
```
- Before the start of the application, make sure you have Environment Variable
```bash
export DJANGO_SETTINGS_MODULE=lisci.settings.local
```

- Start the application
```bash
python3 manage.py runserver 
```