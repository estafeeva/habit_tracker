




pip install django==4.2 python-dotenv psycopg2
django-admin startproject config .
python manage.py startapp habits
python manage.py startapp users
pip install djangorestframework djangorestframework-simplejwt django-filter
pip install pillow
python manage.py makemigrations
python manage.py migrate
python manage.py csu
pip install celery django-celery-beat redis eventlet
pip install black
pip install telebot
python manage.py migrate
pip install django-cors-headers
pip install drf-yasg coverage flake8

redis-server
celery -A config worker -l INFO -P eventlet
celery -A config beat --loglevel INFO
