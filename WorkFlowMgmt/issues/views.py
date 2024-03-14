from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.utils import timezone

from base.models import Issue
from base.forms import IssueForm


class IssuesListView(ListView):
    template_name = 'issues/issue_list.html'
    model = Issue
    context_object_name = 'issues'
    
    def get_queryset(self):
        return Issue.objects.all()


class IssueCreateView(CreateView):
    template_name = 'issues/create_issue.html'
    model = Issue
    form_class = IssueForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.upload_date = timezone.now()
        
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('issues:issue_list')


class IssueDetailView(DetailView):
    template_name = 'issues/issue_detail.html'
    model = Issue
    context_object_name = 'issue'
    
    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=pk)
        return issue