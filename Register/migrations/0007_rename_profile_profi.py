# Generated by Django 4.0.3 on 2022-06-10 08:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Register', '0006_alter_profile_city_alter_profile_state_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='profi',
        ),
    ]