# Generated by Django 2.0.8 on 2018-09-30 19:12

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('fiu_app', '0004_advertisement_redirect_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', tinymce.models.HTMLField()),
            ],
        ),
        migrations.AlterField(
            model_name='addon',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='details',
            field=tinymce.models.HTMLField(verbose_name='Advertisement Details'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='facility',
            name='bio',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='giftcertificate',
            name='details',
            field=tinymce.models.HTMLField(verbose_name='Gift Certificate Details'),
        ),
        migrations.AlterField(
            model_name='package',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
