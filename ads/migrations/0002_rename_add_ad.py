# Generated by Django 4.2 on 2024-04-09 17:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Add',
            new_name='Ad',
        ),
    ]
