# Generated by Django 4.1.3 on 2022-11-30 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_remove_customer_customer_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Customer_password',
            field=models.CharField(default='', max_length=20),
        ),
    ]
