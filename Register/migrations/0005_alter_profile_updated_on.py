# Generated by Django 4.0.3 on 2022-06-10 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0004_alter_profile_ph_pro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
