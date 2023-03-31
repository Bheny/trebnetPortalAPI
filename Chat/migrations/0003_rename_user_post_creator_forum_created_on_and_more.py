# Generated by Django 4.1.7 on 2023-03-30 16:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0012_remove_profile_class_profile_class'),
        ('Ranks', '0002_rank_tag_alter_rank_title'),
        ('Chat', '0002_forum_thread_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='creator',
        ),
        migrations.AddField(
            model_name='forum',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='forum',
            name='creator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Profiles.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forum',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='forum',
            name='rank',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Ranks.rank'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forum',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='room',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='room',
            name='creator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='Profiles.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='room',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thread',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='thread',
            name='creator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Profiles.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thread',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='thread',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]