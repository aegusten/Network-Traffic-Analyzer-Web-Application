bind = '0.0.0.0:8000'
workers = 3  
backlog = 2048
debug = False 
proc_name = 'gunicorn.pid'
pidfile = '/var/log/gunicorn/debug.log'
loglevel = 'info' 
