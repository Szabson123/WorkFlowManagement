from django.shortcuts import render, reverse
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
        return reverse('database:machines_list')
