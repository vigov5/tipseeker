#!/bin/sh
echo "Waiting for database at tipseeker_db:3306"
wait-for tipseeker_db:3306 -t 60 -q -- echo OK
alembic upgrade head
gunicorn --bind 0.0.0.0:5000 app:app
