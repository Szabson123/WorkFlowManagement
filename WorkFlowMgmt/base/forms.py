from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from base.models import Profile, User, Task, MachineDatabase, MachineModifications, MachineFixes, MachineChanges


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
        fields = ['name', 'documentations', 'description', 'image']


class MachineModificationForm(forms.ModelForm):
    class Meta:
        model = MachineModifications
        fields = ['name','modification', 'photos']


class MachineChangesForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=MachineDatabase.objects.all(), empty_label=None)
    class Meta:
        model = MachineChanges
        fields = ['changes', 'photos']


class MachineFixesForm(forms.ModelForm):
    class Meta:
        model = MachineFixes
        fields = ['name', 'fixes', 'photos']

