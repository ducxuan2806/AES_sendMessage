# Generated by Django 5.0 on 2023-12-30 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_rename_privatekey_userprofile_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friends',
            old_name='privateKey',
            new_name='key',
        ),
    ]
