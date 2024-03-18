from django.db import models
from django.contrib.auth.models import User


PRIORITY_CHOICES = (
    ('0', 'Brak'),
    ('1', 'Wysoki'),
    ('2', 'Średni'),
    ('3', 'Niski'),
)

TYPE_CHOICES = (
    ('0', 'Awaria'),
    ('1', 'Przezbrojenie'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    number = models.DecimalField(decimal_places=0, max_digits=11, null=True, blank=True)
    your_employees = models.ManyToManyField(User, blank=True, related_name='your_employees')

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


class MachineDatabase(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='machines_images/')
    documentations = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class MachineModifications(models.Model):
    machine = models.ForeignKey(MachineDatabase, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    photos = models.ImageField(blank=True, null=True, upload_to='modifications_images/')
    modification = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}'    


class MachineFixes(models.Model):
    machine = models.ForeignKey(MachineDatabase, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    photos = models.ImageField(blank=True, null=True, upload_to='fixes_images/')
    fixes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}'    
    
    
class MachineChanges(models.Model):
    machine = models.ForeignKey(MachineDatabase, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    photos = models.ImageField(blank=True, null=True, upload_to='changes_images/')
    changes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
    
    
class Issue(models.Model):
    author = models.ForeignKey(User, related_name='authored_issues', on_delete=models.CASCADE)
    accepted_by = models.ForeignKey(User, related_name='accepted_issues', on_delete=models.CASCADE, blank=True, null=True)
    upload_date = models.DateTimeField()
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    line = models.CharField(max_length=255)
    machine = models.ForeignKey(MachineDatabase, on_delete=models.CASCADE)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='0')
    type_of_issue = models.CharField(max_length=1, choices=TYPE_CHOICES, blank=True, null=True)
    
    def __str__(self):
        return f'{self.title}'


class Forum(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='forum_images/')