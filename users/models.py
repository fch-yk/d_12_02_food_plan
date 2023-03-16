from django.db import models
from django.contrib.auth.models import AbstractUser
from food.models import Subscription, Dish


class User(AbstractUser):
    subscription = models.ForeignKey(
        Subscription,
        related_name='users',
        verbose_name='Подписка',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    subscription_start_at = models.DateField(
        'Старт подписки',
        blank=True,
        null=True
    )
    liked_dishes = models.ManyToManyField(
        Dish,
        related_name='liked_dishs',
        verbose_name='Лайкнутые блюда',
        blank=True,
    )
    disliked_dishes = models.ManyToManyField(
        Dish,
        related_name='disliked_dishs',
        verbose_name='Дизлайкнутые блюда',
        blank=True,
    )
    avatar = models.ImageField(
        upload_to='users_images',
        blank=True,
    )
