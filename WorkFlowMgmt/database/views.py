from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from base.models import MachineDatabase, MachineHistory
from base.forms import (MachineCreateForm, MachineModificationForm,
                        MachineFixesForm, MachineChangesForm)


class MachinesListView(ListView):
    template_name = 'database/machines_list.html'
    model = MachineDatabase
    context_object_name = 'machines'

    def get_queryset(self):
        return MachineDatabase.objects.all()


class CreateNewMachineView(CreateView):
    template_name = 'database/create_machine.html'
    model = MachineDatabase
    form_class = MachineCreateForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('database:database')


class MachineDetailView(DetailView):
    template_name = 'database/machine_detail.html'
    model = MachineDatabase
    context_object_name = 'machine'
    
    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        machine = get_object_or_404(MachineDatabase, pk=pk)
        return machine
    
    
class MachineModificationListView(ListView):
    template_name = 'database/modyfications_list.html'
    model = MachineHistory
    context_object_name = 'modyfications'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        machine = get_object_or_404(MachineDatabase, pk=pk)
        context['machine'] = machine
        return context
    
    def get_queryset(self):
        return MachineHistory.objects.all()
    

class MachineModificationCreateView(CreateView):
    template_name = 'database/create_modyfication.html'
    model = MachineHistory
    form_class = MachineModificationForm
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse('database:modyfications_list')
    

class MachineModyficationDetailView(DetailView):
    template_name = 'database/modyfication_detail.html'
    model = MachineHistory
    
    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        modyfication = get_object_or_404(MachineHistory, pk=pk)
        return modyfication