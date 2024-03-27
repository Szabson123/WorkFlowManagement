from django.shortcuts import render
from django.views.generic import ListView

from base.models import Forum, Comments


class MainForumPage(ListView):
    model = Forum
    template_name = 'forum/main_page.html'
    context_object_name = 'post'
    
    def get_queryset(self): 
        return Forum.objects.all()