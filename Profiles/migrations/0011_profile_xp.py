# Generated by Django 4.1.7 on 2023-03-20 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Profiles", "0010_profile_balance"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="xp",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
