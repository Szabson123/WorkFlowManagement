# Generated by Django 4.2.6 on 2024-03-27 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_forum_author_forum_end_date_forum_upload_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='active',
            field=models.BooleanField(default='True'),
        ),
    ]
