#!/bin/sh
if  [ "$DEBUG" = "0" ]
then
    if [ "$POSTGRES_DB" = "django_awards" ]
    then
        echo "Waiting for postgres..."

        while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
            sleep 0.1
        done

        echo "PostgreSQL started"
    fi

    python manage.py flush --no-input
    python manage.py migrate

    exec "$@"
else
    while true; do
        echo "Re-starting Django runserver"
        python manage.py runserver 0.0.0.0:8000 || sleep 2
    done
fi

done