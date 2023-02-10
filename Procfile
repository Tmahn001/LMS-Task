web: gunicorn LMS.wsgi:application && worker: celery -A LMS worker --loglevel=info -P eventlet
