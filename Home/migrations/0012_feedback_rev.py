# Generated by Django 4.0.3 on 2022-05-28 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0011_remove_feedback_rev_feedback_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='rev',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
