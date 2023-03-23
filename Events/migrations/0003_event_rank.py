# Generated by Django 4.1.7 on 2023-03-20 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Ranks", "0002_rank_tag_alter_rank_title"),
        ("Events", "0002_remove_event_attendants_event_has_ended_attendance"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="rank",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="Ranks.rank"
            ),
            preserve_default=False,
        ),
    ]