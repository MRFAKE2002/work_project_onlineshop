# Generated by Django 4.1.4 on 2023-05-15 18:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_product_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 18, 23, 40, 975735, tzinfo=datetime.timezone.utc), verbose_name='published'),
        ),
    ]