# Generated by Django 2.0.8 on 2018-10-13 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiu_app', '0012_auto_20181006_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Advertisement Title'),
        ),
    ]
