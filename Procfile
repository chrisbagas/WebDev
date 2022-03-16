migrate: bash deployment.sh
release: python manage.py migrate
web: gunicorn webdev.wsgi --log-file -
