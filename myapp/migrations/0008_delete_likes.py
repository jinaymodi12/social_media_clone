# Generated by Django 4.0.5 on 2022-06-03 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_addpost_dislike_addpost_like'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Likes',
        ),
    ]
