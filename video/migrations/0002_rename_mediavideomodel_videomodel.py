# Generated by Django 5.0.7 on 2024-08-03 01:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MediaVideoModel',
            new_name='VideoModel',
        ),
    ]
