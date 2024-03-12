from django.contrib import admin
from base.models import Profile, Task, MachineDatabase, MachineHistory

admin.site.register(Profile)
admin.site.register(Task)
admin.site.register(MachineDatabase)
admin.site.register(MachineHistory)


