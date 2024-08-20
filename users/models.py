from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import UserManager


class UserRoles(models.TextChoices):
    """Роли пользователя:
    user - может получать список объявлений, получать одно объявление, создавать объявление,
    редактировать и удалять свое объявление, получать список комментариев, создавать комментарии,
    редактировать/удалять свои комментарии.
    admin - может дополнительно к правам пользователя редактировать или удалять объявления и
    комментарии любых других пользователей.
    """

    USER = "user"
    ADMIN = "admin"


class User(AbstractUser):
    """Модель пользователя"""

    username = None

    first_name = models.CharField(
        max_length=150,
        verbose_name="имя пользователя",
        blank=True,
        null=True,
        help_text="Укажите имя",
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name="фамилия пользователя",
        blank=True,
        null=True,
        help_text="Укажите фамилию",
    )
    phone_number = models.CharField(
        max_length=35,
        verbose_name="номер телефона",
        blank=True,
        null=True,
        help_text="Укажите номер телефона",
    )
    avatar = models.ImageField(
        upload_to="users/",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите аватар",
    )
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Укажите электронную почту"
    )
    role = models.CharField(
        max_length=10,
        choices=UserRoles.choices,
        default="user",
        verbose_name="статус пользователя",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Аккаунт активен",
        help_text="Укажите, активен ли аккаунт")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    objects = UserManager()
    # менеджер объектов
