# Generated by Django 2.1 on 2020-09-13 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Interior_app', '0012_customer_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video_upload_professional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videofile', models.FileField(null=True, upload_to='videos/', verbose_name='')),
                ('post_video', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Interior_app.Profile')),
            ],
        ),
    ]
