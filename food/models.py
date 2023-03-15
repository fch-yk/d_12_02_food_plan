from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=50
    )
    price = models.DecimalField(
        'цена',
        max_digits=15,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return self.title


class Dish(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=50
    )
    description = models.TextField(
        verbose_name='описание',
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


class DishItem(models.Model):
    dish = models.ForeignKey(
        Dish,
        related_name='items',
        verbose_name="блюдо",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        related_name='dish_items',
        verbose_name='продукт',
        on_delete=models.PROTECT,
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name='количество',
        validators=[MinValueValidator(1)],
    )

    class Meta:
        verbose_name = 'ингридиент'
        verbose_name_plural = 'ингридиенты'


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
