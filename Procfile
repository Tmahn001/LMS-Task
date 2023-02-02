web: python manage.py migrate && celery -A myapp.celeryapp worker --loglevel=info -P eventlet && gunicorn LMS.wsgi

