# Generated by Django 3.2.4 on 2024-08-02 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='farmer',
        ),
    ]
