# Generated by Django 3.2.4 on 2024-08-02 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Farmers', '0003_account_farmer'),
        ('Products', '0002_remove_product_farmer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='unit_price',
        ),
        migrations.AddField(
            model_name='product',
            name='farmer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Farmers.farmer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Rejected')], default='pending'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=50, unique=True)),
                ('quantity', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Paid'), (2, 'Cancelled')], default=0)),
                ('delivery', models.IntegerField(choices=[(0, 'Packaging'), (1, 'Shipped'), (2, 'Delivered')], default=0)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Farmers.farmer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product')),
            ],
        ),
    ]
