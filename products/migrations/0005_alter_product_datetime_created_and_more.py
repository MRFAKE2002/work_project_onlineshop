# Generated by Django 4.1.4 on 2022-12-30 18:26

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_comment_active_comment_datetime_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 18, 26, 42, 480010, tzinfo=datetime.timezone.utc), verbose_name='datetime_created'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]