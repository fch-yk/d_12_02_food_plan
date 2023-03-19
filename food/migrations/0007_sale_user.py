# Generated by Django 4.1.7 on 2023-03-19 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0006_dish_meals'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sales', to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]