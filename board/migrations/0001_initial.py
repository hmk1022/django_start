# Generated by Django 4.0.2 on 2022-02-04 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('addr', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=3)),
                ('age', models.CharField(max_length=3)),
                ('interest', models.CharField(max_length=3)),
                ('hp', models.CharField(max_length=20)),
                ('create_date', models.DateTimeField()),
            ],
        ),
    ]
