# Generated by Django 4.2.4 on 2023-08-24 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articleapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="like",
            field=models.IntegerField(default=0),
        ),
    ]