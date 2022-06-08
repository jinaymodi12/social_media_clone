# Generated by Django 4.0.5 on 2022-06-03 09:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_delete_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addpost',
            name='dislike',
        ),
        migrations.AlterField(
            model_name='addpost',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='lik', to=settings.AUTH_USER_MODEL),
        ),
    ]
