from django.urls import path
from database.views import *

app_name = 'database'

urlpatterns = [
    path('', MachinesListView.as_view(), name='database'),
    path('create_machine', CreateNewMachineView.as_view(), name='create_machine'),
    path('machine_detail/<int:pk>/', MachineDetailView.as_view(), name='machine_detail'),
    
    path('machine_detail/<int:pk>/modyfication_list/', MachineModificationListView.as_view(), name='machine_modification_list'),
    path('machine_detail/<int:pk>/create_modyfication/', MachineModificationCreateView.as_view(), name='create_modyfications'),
    path('machine_detail/<int:pk>/modyfication_detail/<int:modyfication_pk>/', MachineModyficationDetailView.as_view(), name='modyfication_detail'),
    
    path('machine_detail/<int:pk>/fix_list/', MachineFixesListView.as_view(), name='fixes_list'),
    path('machine_detail/<int:pk>/create_fix/', MachineFixesCreateView.as_view(), name='create_fix'),
    path('machine_detail/<int:pk>/fix_detail/<int:fix_pk>/', MachineFixesDetailView.as_view(), name='fix_detail'),
    
    path('machine_detail/<int:pk>/changes_list/', MachineChangesListView.as_view(), name='changes_list'),
    path('machine_detail/<int:pk>/create_change/', MachineChangesCreateView.as_view(), name='create_change'),
    path('machine_detail/<int:pk>/change_detail/<int:change_pk>/', MachineChangesDetailView.as_view(), name='change_detail'),

]
