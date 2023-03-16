# Generated by Django 4.1.7 on 2023-03-16 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_dishcategory_dish_categories'),
        ('users', '0002_alter_user_disliked_dishes_alter_user_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'пользователь', 'verbose_name_plural': 'пользователи'},
        ),
        migrations.AddField(
            model_name='user',
            name='allergy_to',
            field=models.ManyToManyField(blank=True, related_name='allergics', to='food.dishcategory', verbose_name='аллергия на'),
        ),
    ]
