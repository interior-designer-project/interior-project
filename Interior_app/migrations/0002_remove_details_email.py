# Generated by Django 2.1 on 2019-07-08 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Interior_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='email',
        ),
    ]
