# Generated by Django 3.0.8 on 2020-12-03 10:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('API2', '0002_auto_20201203_1417'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='UserProfile',
        ),
    ]
