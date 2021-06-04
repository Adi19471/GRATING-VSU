# Generated by Django 3.0 on 2021-05-28 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile_no', models.IntegerField()),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('adhar', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=115)),
            ],
        ),
    ]