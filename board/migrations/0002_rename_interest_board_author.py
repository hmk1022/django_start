# Generated by Django 4.0.2 on 2022-02-04 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='interest',
            new_name='author',
        ),
    ]
