# Generated by Django 5.0.1 on 2024-03-08 12:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_task_assigned_to_task_creator'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='your_employees',
            field=models.ManyToManyField(blank=True, related_name='your_employees', to=settings.AUTH_USER_MODEL),
        ),
    ]
