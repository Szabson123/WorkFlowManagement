from django.contrib import admin
from base.models import Profile, Task, MachineDatabase, MachineChanges, MachineFixes, MachineModifications, Issue, Forum, Tag

admin.site.register(Profile)
admin.site.register(Task)
admin.site.register(MachineDatabase)
admin.site.register(MachineChanges)
admin.site.register(MachineFixes)
admin.site.register(MachineModifications)
admin.site.register(Issue)
admin.site.register(Forum)
admin.site.register(Tag)
