# Generated by Django 4.0.3 on 2022-05-19 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
