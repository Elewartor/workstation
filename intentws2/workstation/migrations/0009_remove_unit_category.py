# Generated by Django 3.0.7 on 2020-10-23 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workstation', '0008_auto_20201023_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='category',
        ),
    ]