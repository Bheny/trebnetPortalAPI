# Generated by Django 3.2.15 on 2022-09-09 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_rank_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='rank',
            name='rank_type',
            field=models.CharField(choices=[('Job', 'Job'), ('Membership', 'Membership')], default='N/A', max_length=100),
        ),
    ]