# Generated by Django 3.0.6 on 2022-01-08 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_event_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='reciever',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reciever', to='api.Profile'),
        ),
    ]
