from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.utils import timezone

from base.models import MachineDatabase, MachineChanges, MachineFixes, MachineModifications
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
    model = MachineModifications
    context_object_name = 'modyfications'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        machine = get_object_or_404(MachineDatabase, pk=pk)
        context['machine'] = machine
        return context
    
    def get_queryset(self):
        machine_pk = self.kwargs.get('pk')
        return MachineModifications.objects.filter(machine__pk=machine_pk)
    

class MachineModificationCreateView(CreateView):
    template_name = 'database/create_modyfication.html'
    model = MachineModifications
    form_class = MachineModificationForm
    
    def form_valid(self, form):
        machine_pk = self.kwargs.get('pk')
        machine = get_object_or_404(MachineDatabase, pk=machine_pk)
        
        form.instance.machine = machine
        form.instance.author = self.request.user
        form.instance.time = timezone.now()
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse('database:database')
    

class MachineModyficationDetailView(DetailView):
    template_name = 'database/modyfication_detail.html'
    model = MachineModifications
    context_object_name = 'modification'
    
    def get_object(self):
        modyfication_pk = self.kwargs.get('modyfication_pk')
        return get_object_or_404(MachineModifications, pk=modyfication_pk)
    
    
class MachineFixesListView(ListView):
    template_name = 'database/fixes_list.html'
    model = MachineFixes
    context_object_name = 'fixes'
    
    def get_queryset(self):
        machine_pk = self.kwargs.get('pk')
        return MachineFixes.objects.filter(machine__pk= machine_pk)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        machine = get_object_or_404(MachineDatabase, pk=pk)
        context['machine'] = machine
        return context
    
    
class MachineFixesCreateView(CreateView):
    template_name = 'database/create_fix.html'
    model = MachineFixes
    form_class = MachineFixesForm
    
    def form_valid(self, form):
        machine_pk = self.kwargs.get('pk')
        machine = get_object_or_404(MachineDatabase, pk=machine_pk)
        
        form.instance.author = self.request.user
        form.instance.time = timezone.now()
        form.instance.machine = machine
        
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse('database:database')
    

class MachineFixesDetailView(DetailView):
    template_name = 'database/fix_detail.html'
    model = MachineFixes
    context_object_name = 'fix'
    
    def get_object(self):
        fix_pk = self.kwargs.get('fix_pk')
        return get_object_or_404(MachineFixes, pk=fix_pk)
    
    
class MachineChangesListView(ListView):
    template_name = 'database/changes_list.html'
    model = MachineChanges
    context_object_name = 'changes'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        machine = get_object_or_404(MachineDatabase, pk=pk)
        context['machine'] = machine
        return machine
    
    def get_queryset(self):
        machine_pk = self.kwargs.get('pk')
        return MachineChanges.objects.filter(machine__pk=machine_pk)
    

class MachineChangesCreateView(CreateView):
    template_name = 'database/create_change.html'
    model = MachineChanges
    
    def form_valid(self, form):
        machine_pk = self.kwargs.get('pk')
        machine = get_object_or_404(MachineDatabase, pk=machine_pk)
        
        form.instance.machine = machine
        form.instance.time = timezone.now()
        form.instance.author = self.request.user
        
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse('database:database')
    

class MachineChangesDetailView(DetailView):
    template_name = 'database/change_detail.html'
    model = MachineChanges
    context_object_name = 'change'
    
    def get_object(self):
        change_pk = self.kwargs.get('change_pk')
        return get_object_or_404(MachineChanges, pk=change_pk) 