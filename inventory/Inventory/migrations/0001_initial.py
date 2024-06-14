# Generated by Django 5.0.6 on 2024-06-14 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('sku', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('initial_stock_level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=15)),
                ('role', models.CharField(choices=[('admin', 'admin'), ('user', 'user')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('stock_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('type', models.CharField(choices=[('in', 'in'), ('out', 'out')], max_length=3)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('contact_info', models.TextField()),
                ('products_supplied', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.product')),
            ],
        ),
    ]
