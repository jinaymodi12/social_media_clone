# Generated by Django 4.0.5 on 2022-06-06 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_remove_user_follower_remove_user_following_follower'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follower',
            old_name='follower',
            new_name='followers',
        ),
    ]