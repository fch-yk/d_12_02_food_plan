# Generated by Django 4.1.7 on 2023-03-15 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.ImageField(blank=True, upload_to='images', verbose_name='картинка'),
        ),
    ]