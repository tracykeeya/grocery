# Generated by Django 5.0.4 on 2024-10-20 12:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0010_remove_stocks_approval_status_alter_sale_stock_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='stock_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 20, 15, 5, 16, 112103)),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='stock_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 20, 15, 5, 16, 110092)),
        ),
    ]
