from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователь:
    все поля от обычного пользователя, но авторизация по email;
    телеграм;
    телефон;
    город;
    аватарка.
    """

    username = None
    email = models.EmailField(
        unique=True,
        verbose_name="Email"
    )
    tg = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name="Telegram_id"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    city = models.CharField(
        max_length=35,
        verbose_name="Город",
        blank=True,
        null=True,
        help_text="Введите город",
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        blank=True,
        null=True,
        help_text="Загрузите аватар",
    )

    token = models.CharField(
        max_length=100,
        verbose_name="Token",
        blank=True,
        null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
