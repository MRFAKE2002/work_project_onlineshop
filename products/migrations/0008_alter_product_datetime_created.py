# Generated by Django 4.1.4 on 2022-12-31 17:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_datetime_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 31, 17, 59, 55, 53649, tzinfo=datetime.timezone.utc), verbose_name='datetime_created'),
        ),
    ]
