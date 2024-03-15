from django.urls import path
from issues.views import *

app_name = 'issues'

urlpatterns = [
    path('', IssuesListView.as_view(), name='issue_list'),
    path('create_issue/', IssueCreateView.as_view(), name='create_issue'),
    path('detail_issue/<int:pk>/', IssueDetailView.as_view(), name='issue_detail'),
    
    path('issue/accept/', IssuesListView.as_view(), name='accept_issue'),
]