# Generated by Django 4.0.3 on 2022-05-29 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0016_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='usr',
            new_name='user',
        ),
    ]