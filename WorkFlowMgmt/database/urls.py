from django.urls import path
from database.views import MachinesListView, CreateNewMachineView

app_name = 'database'

urlpatterns = [
    path('', MachinesListView.as_view(), name='database'),
    path('create_machine', CreateNewMachineView.as_view(), name='create_machine')
]
