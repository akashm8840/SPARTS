# Generated by Django 4.0.3 on 2022-06-07 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0002_rename_user_profile_usr_remove_profile_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ph_pro',
            field=models.BigIntegerField(default='123456789'),
        ),
        migrations.AddField(
            model_name='profile',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]