# Generated by Django 3.2.3 on 2021-05-31 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizji', '0002_auto_20210531_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.TextField(verbose_name='Title'),
        ),
    ]
