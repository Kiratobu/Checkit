# Generated by Django 4.0.6 on 2022-07-12 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_notification_event_notifications'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userparticipant',
            old_name='event_id',
            new_name='event_participant',
        ),
        migrations.RenameField(
            model_name='userparticipant',
            old_name='user_id',
            new_name='user_participant',
        ),
    ]
