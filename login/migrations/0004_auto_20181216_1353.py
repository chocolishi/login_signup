# Generated by Django 2.1.4 on 2018-12-16 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20181216_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='identification_photo',
        ),
        migrations.RemoveField(
            model_name='user',
            name='resume',
        ),
    ]
