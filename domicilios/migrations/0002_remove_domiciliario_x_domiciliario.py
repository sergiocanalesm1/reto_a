# Generated by Django 3.1 on 2020-08-12 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domicilios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domiciliario',
            name='x_domiciliario',
        ),
    ]
