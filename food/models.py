from django.core.validators import MinValueValidator
from django.db import models


class Dish(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=50
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )

    recipe = models.TextField(
        verbose_name='рецепт',
        blank=True,
    )

    image = models.ImageField(
        'картинка',
        upload_to='images',
        blank=True,
    )

    class Meta:
        verbose_name = 'блюдо'
        verbose_name_plural = 'блюда'

    def __str__(self):
        return self.title


class Subscription(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=50
    )
    duration = models.PositiveSmallIntegerField(
        verbose_name='количество',
        validators=[MinValueValidator(1)],
    )
    price = models.DecimalField(
        'цена',
        max_digits=15,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'

    def __str__(self):
        return self.title


class Sale(models.Model):
    sum = models.DecimalField(
        'цена',
        max_digits=15,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    payed_at = models.DateTimeField(
        verbose_name='дата оплаты',
        db_index=True,
    )

    class Meta:
        verbose_name = 'продажа'
        verbose_name_plural = 'продажи'
