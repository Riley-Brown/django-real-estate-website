# Generated by Django 2.1.4 on 2018-12-28 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_realtor_testing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realtor',
            name='testing',
        ),
    ]
