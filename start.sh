#!/bin/bash
ps -aux | grep 8007 | awk '{print $2}' | xargs kill -9
gunicorn StudentManageSys.wsgi:application -b 0.0.0.0:8007 -w 4 -t 300 --reload