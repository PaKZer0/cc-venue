#!/bin/sh

if [ "$DATABASE" = "postgres" ]; then
    echo "Waiting for postgres..."

    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Make migrations and migrate the database.
echo "Making migrations and migrating the database. "
python manage.py makemigrations guard --noinput 
python manage.py migrate --noinput 
python manage.py collectstatic --noinput

if [[  ${SERVER_TYPE} = "dev" ]]; then
    echo "Running django development server"
    exec /code/manage.py runserver 0:8080
else
    echo "Running gunicorn production server"
    exec gunicorn vaktapp.wsgi:application --bind 0.0.0.0:8080 --workers=4 --threads=4
fi
