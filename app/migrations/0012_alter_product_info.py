# Generated by Django 4.1.4 on 2023-05-17 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_order_transaction_id_product_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='info',
            field=models.TextField(null=True),
        ),
    ]
