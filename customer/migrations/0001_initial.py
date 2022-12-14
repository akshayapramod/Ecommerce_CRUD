# Generated by Django 4.1.3 on 2022-11-30 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_name', models.CharField(max_length=20)),
                ('Customer_number', models.BigIntegerField()),
                ('Customer_address', models.CharField(max_length=100)),
                ('Customer_password', models.CharField(max_length=20)),
                ('Customer_gender', models.CharField(max_length=10)),
                ('Customer_email', models.CharField(max_length=20)),
            ],
        ),
    ]
