# Generated by Django 4.2.6 on 2024-03-11 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_machinedatabase_machinehistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machinedatabase',
            name='documentations',
            field=models.TextField(blank=True, null=True),
        ),
    ]