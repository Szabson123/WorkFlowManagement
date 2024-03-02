from django.shortcuts import render
from django.views.generic import ListView

from base.models import Task


class TaskListView(ListView):
    model = Task
    template_name = 'todo/tasks'
    context_object_name = 'tasks'

    def get_queryset(self):
        Task.objects.filter(assignet_to__in=[self.request.user])

