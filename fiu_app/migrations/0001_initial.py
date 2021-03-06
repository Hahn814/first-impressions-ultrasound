# Generated by Django 2.0.8 on 2018-09-29 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddOn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='img/addons/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.TextField()),
                ('city', models.TextField()),
                ('province', models.TextField()),
                ('code', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('phone_number', models.IntegerField()),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fiu_app.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('image', models.ImageField(upload_to='img/facilites/')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fiu_app.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='photos', verbose_name='My Photo')),
                ('gallery', models.ManyToManyField(to='fiu_app.Gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fiu_app.Package')),
            ],
        ),
        migrations.AddField(
            model_name='addon',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fiu_app.Package'),
        ),
    ]
