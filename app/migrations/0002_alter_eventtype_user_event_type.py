# Generated by Django 4.0.6 on 2022-08-17 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtype',
            name='user_event_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_e_t', to=settings.AUTH_USER_MODEL),
        ),
    ]
