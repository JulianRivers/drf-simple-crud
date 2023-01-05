#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requerimients.txt

python manage.py collectstatic --no-input
python manage.py makemigrations
ython manage.py makemigrations projects
python manage.py migrate
python manage.py migrate projects