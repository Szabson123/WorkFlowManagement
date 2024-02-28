from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    number = models.DecimalField(decimal_places=0, max_digits=11, null=True, blank=True)

    def __str__(self):
        return f'{self.user}'
