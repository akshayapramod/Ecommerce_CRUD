# Generated by Django 4.1.3 on 2022-11-30 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='Customer_password',
        ),
    ]
