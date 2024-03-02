from django.shortcuts import render
from django.views.generic import ListView

from base.models import Task


class TaskListView(ListView):
    model = Task
    template_name = 'todo/tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        Task.objects.filter(assigned_to__in=[self.request.user])

