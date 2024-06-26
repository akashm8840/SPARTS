# Generated by Django 4.0.3 on 2022-05-30 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='usr',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='cnum',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='pimg',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='updated_on',
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.TextField(default='Not Available'),
        ),
        migrations.AddField(
            model_name='profile',
            name='img_pro',
            field=models.ImageField(default='default\\default_imgpro.jpg', upload_to='media'),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.TextField(default='Not Available'),
        ),
        migrations.AddField(
            model_name='profile',
            name='street',
            field=models.TextField(default='Not Available'),
        ),
    ]
