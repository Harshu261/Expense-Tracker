# Generated by Django 5.2 on 2025-04-06 07:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_rename_abs_price_mainitem_cost_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='platesale',
            name='main_item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='plate_sales', to='sales.mainitem'),
        ),
    ]
