# Generated by Django 4.1.6 on 2023-03-08 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Profiles", "0002_profile_is_driver_profile_is_verified"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="rating",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]