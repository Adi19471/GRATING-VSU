# Generated by Django 3.0 on 2021-05-28 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form_app', '0002_auto_20210528_1543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='adhar',
            new_name='adharDetailes',
        ),
        migrations.AlterField(
            model_name='register',
            name='address',
            field=models.CharField(max_length=250),
        ),
    ]
