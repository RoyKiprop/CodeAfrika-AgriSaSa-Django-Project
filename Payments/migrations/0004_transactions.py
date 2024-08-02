# Generated by Django 3.2.4 on 2024-08-02 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Farmers', '0003_account_farmer'),
        ('Payments', '0003_delete_transactions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_type', models.IntegerField(choices=[(0, 'Deposit'), (1, 'Withdrawal'), (2, 'Commission'), (3, 'Subscription'), (4, 'Orders')], default=0)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Farmers.account')),
            ],
        ),
    ]
