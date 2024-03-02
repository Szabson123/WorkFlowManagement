from django.urls import path
from todo.views import TaskListView

app_name = 'todo'


urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='tasks')
]