# Generated by Django 3.0.7 on 2020-06-18 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workstation', '0004_unit_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='details',
            field=models.TextField(blank=True, max_length=9000, null=True),
        ),
    ]
