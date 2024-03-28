from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse, reverse_lazy
from django.utils import timezone

from base.models import Forum, Comments
from base.forms import ForumForm


class MainForumPage(ListView):
    model = Forum
    template_name = 'forum/forum.html'
    context_object_name = 'posts'
    
    def get_queryset(self): 
        return Forum.objects.all()
    

class MyPostsListView(ListView):
    model = Forum
    context_object_name = 'posts'
    template_name = 'forum/my_posts.html'
    
    def get_queryset(self):
        return Forum.objects.filter(author=self.request.user)


class CreatePostView(CreateView):
    template_name = 'forum/new_post.html'
    model = Forum
    form_class = ForumForm
    success_url = reverse_lazy('forum:forum')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.upload_date = timezone.now()
        return super().form_valid(form)


class PostDetailView(DetailView):
    template_name = 'forum/post_detail.html'
    model = Forum
    context_object_name = 'post'
    
    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        post = get_object_or_404(Forum, pk=pk)
        return post