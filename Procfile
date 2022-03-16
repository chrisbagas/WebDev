migrate: bash deployment.sh
release: python manage.py migrate --run-syncdb
web: gunicorn webdev.wsgi --log-file -
