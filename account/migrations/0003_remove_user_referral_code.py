# Generated by Django 4.0.6 on 2022-07-13 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_referral_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='referral_code',
        ),
    ]
