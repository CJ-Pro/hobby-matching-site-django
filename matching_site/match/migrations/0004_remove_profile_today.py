# Generated by Django 2.1.2 on 2018-12-11 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0003_auto_20181211_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='today',
        ),
    ]
