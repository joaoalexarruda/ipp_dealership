# Generated by Django 5.0.4 on 2024-04-27 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("motorcycles", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="motorcycleinventory",
            name="motorcycle_total_value",
        ),
    ]
