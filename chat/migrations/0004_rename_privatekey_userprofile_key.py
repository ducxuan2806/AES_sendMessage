# Generated by Django 5.0 on 2023-12-30 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_friends_privatekey_userprofile_privatekey'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='privateKey',
            new_name='key',
        ),
    ]
