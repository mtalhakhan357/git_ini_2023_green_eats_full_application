# Generated by Django 4.1.5 on 2023-01-08 16:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MyApi", "0008_alter_getdata_date_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="getdata",
            name="date_created",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 1, 8, 22, 28, 52, 898570)
            ),
        ),
    ]
