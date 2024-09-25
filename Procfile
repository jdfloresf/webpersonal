release: python manage.py collectstatic --noinput
web: python manage.py collectstatic && gunicorn webpersonal.wsgi