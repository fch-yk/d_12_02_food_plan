# Generated by Django 4.1.7 on 2023-03-17 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_meal'),
        ('users', '0003_alter_user_options_user_allergy_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='meals',
            field=models.ManyToManyField(blank=True, related_name='users', to='food.meal', verbose_name='приемы пищи'),
        ),
        migrations.AddField(
            model_name='user',
            name='persons_number',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='количество персон'),
        ),
    ]
