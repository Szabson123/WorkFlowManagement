from django.db import models
from django.contrib.auth.models import User


PRIORITY_CHOICES = (
    ('0', 'Brak'),
    ('1', 'Wysoki'),
    ('2', 'Średni'),
    ('3', 'Niski'),
)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    number = models.DecimalField(decimal_places=0, max_digits=11, null=True, blank=True)

    def __str__(self):
        return f'{self.user}'


class Task(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator_tasks', null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='0')
    assigned_to = models.ManyToManyField(User, related_name='assigned_tasks', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
