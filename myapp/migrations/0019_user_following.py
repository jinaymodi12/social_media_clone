# Generated by Django 4.0.5 on 2022-06-06 08:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_remove_addpost_followers_user_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(related_name='followings', to=settings.AUTH_USER_MODEL),
        ),
    ]