# Generated by Django 4.1.4 on 2023-03-14 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_media', '0007_post_is_saved_post_saved_user_alter_post_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_saved',
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.TimeField(blank=True, default='04:38:22'),
        ),
    ]
