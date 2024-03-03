from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView

from base.models import Task
from base.forms import TaskForm


class TaskListView(ListView):
    model = Task
    template_name = 'todo/tasks_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(assigned_to__in=[self.request.user])


class CreateTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/create_task.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('todo:tasks_list')
