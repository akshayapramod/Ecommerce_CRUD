# Generated by Django 4.1.3 on 2022-12-05 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_alter_seller_acc_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='acc_number',
            field=models.BigIntegerField(default=1),
        ),
    ]
