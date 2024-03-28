from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse, reverse_lazy

from base.models import Forum, Comments
from base.forms import ForumForm


class MainForumPage(ListView):
    model = Forum
    template_name = 'forum/forum.html'
    context_object_name = 'posts'
    
    def get_queryset(self): 
        return Forum.objects.all()
    
    
class CreatePostView(CreateView):
    template_name = 'forum/new_post.html'
    model = Forum
    form_class = ForumForm
    success_url = reverse_lazy('forum:forum')

    def form_valid(self, form):
        return super().form_valid(form)
