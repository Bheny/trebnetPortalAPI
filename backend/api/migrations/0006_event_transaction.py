# Generated by Django 3.0.6 on 2022-01-08 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_auto_20220108_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=20)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now=True)),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reciever', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sender', to='api.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default.png', upload_to='events')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('location', models.CharField(max_length=255)),
                ('date_time', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('attendants', models.ManyToManyField(blank=True, related_name='participants', to='api.Profile')),
            ],
        ),
    ]
