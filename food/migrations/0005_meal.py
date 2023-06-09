# Generated by Django 4.1.7 on 2023-03-17 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_dishcategory_dish_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название')),
                ('position', models.PositiveSmallIntegerField(db_index=True, default=0, verbose_name='Position')),
            ],
            options={
                'verbose_name': 'прием пищи',
                'verbose_name_plural': 'приемы пищи',
                'ordering': ['position'],
            },
        ),
    ]
