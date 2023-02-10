gunicorn LMS.wsgi:application
celery -A LMS worker --loglevel=info -P eventlet
