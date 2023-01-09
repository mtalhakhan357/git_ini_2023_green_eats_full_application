# Generated by Django 4.1.5 on 2023-01-08 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MyApi", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="getdata",
            name="date_created",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 1, 8, 22, 11, 51, 78413)
            ),
        ),
        migrations.AddField(
            model_name="getdata",
            name="image",
            field=models.ImageField(
                default="MyApi/static/foodimages/1072416.jpg",
                upload_to="MyApi/static/foodimages",
            ),
        ),
    ]