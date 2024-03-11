from django.urls import path
from database.views import MachinesListView, CreateNewMachineView, MachineDetailView

app_name = 'database'

urlpatterns = [
    path('', MachinesListView.as_view(), name='database'),
    path('create_machine', CreateNewMachineView.as_view(), name='create_machine'),
    path('machine_detail/<int:pk>/', MachineDetailView.as_view(), name='machine_detail'),
]
