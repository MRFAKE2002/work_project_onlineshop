# Generated by Django 4.1.4 on 2023-02-18 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_product_datetime_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 18, 20, 29, 4, 537429, tzinfo=datetime.timezone.utc), verbose_name='datetime_created'),
        ),
    ]
