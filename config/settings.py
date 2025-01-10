import os
from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "drf_yasg",
    "habits",
    "users",
    "django_filters",
    "rest_framework_simplejwt",
    "django_celery_beat",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("NAME"),
        "USER": os.getenv("USER"),
        "PASSWORD": os.getenv("PASSWORD"),
        "HOST": os.getenv("HOST"),
        "PORT": os.getenv("PORT"),
    }
}

X = "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
Y = "django.contrib.auth.password_validation.MinimumLengthValidator"
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": X,
    },
    {
        "NAME": Y,
    },
    {
        "NAME":
            "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME":
            "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=120),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Настройки для Celery

# URL-адрес брокера сообщений
CELERY_BROKER_URL = os.getenv(
    "REDIS"
)  # Например, Redis, который по умолчанию работает на порту 6379

# URL-адрес брокера результатов, также Redis
CELERY_RESULT_BACKEND = os.getenv("REDIS")

# Часовой пояс для работы Celery
CELERY_TIMEZONE = "Australia/Tasmania"

# Флаг отслеживания выполнения задач
CELERY_TASK_TRACK_STARTED = True

# Максимальное время на выполнение задачи
CELERY_TASK_TIME_LIMIT = 30 * 60
# CELERY_STORE_ERRORS_EVEN_IF_IGNORED = True
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True

CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

CELERY_BEAT_SCHEDULE = {
    "send_message_for_users": {
        "task": "users.tasks.send_message_for_users",  # Путь к задаче
        "schedule": timedelta(
            seconds=10
        ),  # Расписание выполнения задачи (например, каждые 10 минут)
    },
}

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS") == "True"
EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL") == "True"

SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

TG_TOKEN_TO_ACCESS_API = os.getenv("TG_TOKEN_TO_ACCESS_API")

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
]

CSRF_TRUSTED_ORIGINS = [
    "https://read-and-write.example.com",
]

CORS_ALLOW_ALL_ORIGINS = False
