# Generated by Django 4.2.6 on 2024-03-28 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0032_tag_comments_likes_forum_draft_forum_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='draft',
            field=models.BooleanField(default=False),
        ),
    ]