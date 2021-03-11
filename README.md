Дипломная работа. БД.

Запуск проекта.

systemctl start postgresql

Создать или подключить БД

'NAME': 'mydatabase', 'USER': 'admin', 'PASSWORD': 'admin', 'HOST': '127.0.0.1', 'PORT': '5432',

python3 -m venv env

source bin/env/activation

pip3 install django

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
