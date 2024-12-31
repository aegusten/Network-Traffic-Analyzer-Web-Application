bind = '0.0.0.0:8000'
workers = 3 
backlog = 2048
loglevel = 'info'
pidfile = '/var/log/gunicorn/gunicorn.pid'
accesslog = '/var/log/gunicorn/access.log'
errorlog = '/var/log/gunicorn/error.log'
