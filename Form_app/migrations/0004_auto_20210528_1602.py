# Generated by Django 3.0 on 2021-05-28 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form_app', '0003_auto_20210528_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='address',
            field=models.TextField(),
        ),
    ]
