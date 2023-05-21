import os
import multiprocessing

loglevel = 'debug'
errorlog = '-'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

bind = 'localhost:80'
workers = 1

timeout = 1 * 60  # 1 minutes

capture_output = True