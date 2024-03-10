from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from base.models import Profile, User, Task, MachineDatabase, MachineHistory


class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'priority', 'assigned_to']
        widgets = {
            'assigned_to': forms.SelectMultiple(),
        }


class MachineCreateForm(forms.ModelForm):
    class Meta:
        model = MachineDatabase
        fields = ['name', 'documentations']


class MachineModificationForm(forms.ModelForm):
    class Meta:
        model = MachineHistory
        fields = ['name', 'modification', 'photos']


class MachineChangesForm(forms.ModelForm):
    class Meta:
        model = MachineHistory
        fields = ['name', 'changes', 'photos']


class MachineFixesForm(forms.ModelForm):
    class Meta:
        model = MachineHistory
        fields = ['name', 'fixes', 'photos']

