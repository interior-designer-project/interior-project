# Generated by Django 2.1 on 2020-09-16 16:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Interior_app', '0014_auto_20200916_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='story_upload_professional',
            name='story_expiration',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
