from django.urls import path
from todo.views import TaskListView, CreateTaskView

app_name = 'todo'


urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='tasks_list'),
    path('create_task', CreateTaskView.as_view(), name='create_task')
]