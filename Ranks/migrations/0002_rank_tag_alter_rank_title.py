# Generated by Django 4.1.7 on 2023-03-20 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ranks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rank',
            name='tag',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='rank',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]