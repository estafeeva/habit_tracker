# Трекер привычек

### Настройка проекта:
```
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
```
### Запуск работы трекера:
```
python manage.py runserver
redis-server
celery -A config worker -l INFO -P eventlet
celery -A config beat --loglevel INFO
```
### Запуск тестов:
```
coverage run --source='.' manage.py test
coverage report
```
### Запуск проверки flake8:
```
flake8 config/
flake8 users/
flake8 habits/
```
### Создание фикстур
```
python -Xutf8 manage.py dumpdata habits > fixtures/habits_data.json --indent=4
python -Xutf8 manage.py dumpdata users > fixtures/users_data.json --indent=4
python -Xutf8 manage.py dumpdata auth > fixtures/auth_data.json --indent=4
```

## Описание
В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. Заказчик прочитал книгу, впечатлился и обратился к вам с запросом реализовать трекер полезных привычек.

В рамках проекта реализована бэкенд-часть SPA веб-приложения.

## Модели
В книге хороший пример привычки описывается как конкретное действие, которое можно уложить в одно предложение:

```я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]```

За каждую полезную привычку необходимо себя вознаграждать или сразу после делать приятную привычку. Но при этом привычка не должна расходовать на выполнение больше двух минут. Исходя из этого получаем первую модель — «Привычка».

### Привычка:
- **Пользователь** — создатель привычки.
- **Место** — место, в котором необходимо выполнять привычку.
- **Время** — время, когда необходимо выполнять привычку.`
- **Действие** — действие, которое представляет собой привычка.
- **Признак приятной привычки** — привычка, которую можно привязать к выполнению полезной привычки.
- **Связанная привычка** — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных.
- **Периодичность (по умолчанию ежедневная)** — периодичность выполнения привычки для напоминания в днях.
- **Вознаграждение** — чем пользователь должен себя вознаградить после выполнения.
- **Время на выполнение** — время, которое предположительно потратит пользователь на выполнение привычки.
- **Признак публичности** — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки.
- **Полезная привычка** — это само действие, которое пользователь будет совершать и получать за его выполнение определенное вознаграждение (приятная привычка или любое другое вознаграждение).
- **Приятная привычка** — это способ вознаградить себя за выполнение полезной привычки. Приятная привычка указывается в качестве связанной для полезной привычки (в поле «Связанная привычка»).
- **Признак приятной привычки** — булево поле, которые указывает на то, что привычка является приятной, а не полезной.

## Валидаторы
- Исключен одновременный выбор связанной привычки и указания вознаграждения. В модели не может быть заполнено одновременно и поле вознаграждения, и поле связанной привычки. Можно заполнить только одно из двух полей.
- Время выполнения должно быть не больше 120 секунд.
- В связанные привычки могут попадать только привычки с признаком приятной привычки.
- У приятной привычки не может быть вознаграждения или связанной привычки.
- Нельзя выполнять привычку реже, чем 1 раз в 7 дней. Нельзя не выполнять привычку более 7 дней. Например, привычка может повторяться раз в неделю, но не раз в 2 недели. За одну неделю необходимо выполнить привычку хотя бы один раз.

## Пагинация
Для вывода списка привычек реализована пагинация с выводом по 5 привычек на страницу.

## Права доступа
- Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.
- Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.

## Эндпоинты
- Регистрация.
- Авторизация.
- Список привычек текущего пользователя с пагинацией.
- Список публичных привычек.
- Создание привычки.
- Редактирование привычки.
- Удаление привычки.

## Интеграция
Для полноценной работы сервиса реализована работа с отложенными задачами для напоминания о том, в какое время какие привычки необходимо выполнять. Для этого интегрирован сервис с мессенджером Телеграм, который будет заниматься рассылкой уведомлений. (С помощью бота https://t.me/BotFather.)

## Безопасность
Для проекта настроен CORS, чтобы фронтенд мог подключаться к проекту на развернутом сервере.

## Документация
Для реализации экранов силами фронтенд-разработчиков настроен вывод документации (swagger и redoc).

## Тесты
Покрытие тестами - 82%