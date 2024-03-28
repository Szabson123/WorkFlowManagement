from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from base.models import Profile, User, Group, Task, MachineDatabase, MachineModifications, MachineFixes, MachineChanges, Issue, Forum, Comments, Tag


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
    class Meta:
        model = MachineChanges
        fields = ['name','changes', 'photos']


class MachineFixesForm(forms.ModelForm):
    class Meta:
        model = MachineFixes
        fields = ['name', 'fixes', 'photos']


class IssueForm(forms.ModelForm):
    class Meta:
        machine = forms.ModelChoiceField(queryset=MachineDatabase.objects.all(), empty_label=None)
        model = Issue
        fields = ['title', 'description', 'line', 'machine', 'priority', 'type_of_issue']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        

class CommentForm(forms.ModelForm):
    class Meta:
        fields = ['text']
        

class ForumForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Forum
        fields = ['name', 'description', 'draft', 'image', 'tag', 'groups']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None) 
        super(ForumForm, self).__init__(*args, **kwargs)

        if user is not None:
            self.fields['groups'].queryset = Group.objects.all() 
        