# Generated by Django 4.0.3 on 2022-05-19 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_alter_order_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='card_ids',
            new_name='cart_ids',
        ),
    ]