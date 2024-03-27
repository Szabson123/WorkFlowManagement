from django.shortcuts import render
from django.views.generic import ListView

from base.models import Forum, Comments


class MainForumPage(ListView):
    model = Forum
    template_name = 'forum/forum.html'
    context_object_name = 'posts'
    
    def get_queryset(self): 
        return Forum.objects.all()