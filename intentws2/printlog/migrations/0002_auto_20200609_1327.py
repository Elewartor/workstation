# Generated by Django 3.0.7 on 2020-06-09 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printlog',
            name='label_type',
            field=models.CharField(max_length=3),
        ),
    ]
