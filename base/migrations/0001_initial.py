# Generated by Django 4.0.4 on 2022-05-23 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('place_id', models.AutoField(primary_key=True, serialize=False)),
                ('place_name', models.CharField(max_length=100, unique=True)),
                ('place_city', models.CharField(max_length=100)),
                ('place_country', models.CharField(max_length=100)),
                ('place_zip', models.CharField(max_length=100)),
                ('place_address', models.CharField(max_length=100)),
            ],
        ),
    ]
