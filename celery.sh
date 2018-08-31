#!/bin/bash
ps aux | grep 'celery worker' | awk '{print $2}' | xargs kill -9
#celery -A StudentManageSys worker -l info
celery multi start w1 -A StudentManageSys -l info --logfile=/var/log/celery.log.log --pidfile=celerypid.pid
