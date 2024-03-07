from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group

from base.models import Profile


@receiver(post_save, sender=User)
def add_to_user_group(sender, instance, created, **kwargs):
    if created:
        user_group, _ = Group.objects.get_or_create(name='User')
        user_group.user_set.add(instance)
