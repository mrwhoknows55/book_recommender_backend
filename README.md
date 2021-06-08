# Book Recommender Backend

> DSM Project By G2 Batch

## How To Set Up Project Locally?

### Create & Activate Virtualenv

``` shell script
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

``` shell script
pip install -r requirements.txt
```

## Run Project

#### Do Migrations

``` shell script
python manage.py makemigrations
python manage.py migrate
```

#### Run Django server

``` shell script
python manage.py runserver
```