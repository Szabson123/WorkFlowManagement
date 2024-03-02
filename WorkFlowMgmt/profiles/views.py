from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from base.models import Profile


def main_page(request):
    return render(request, 'profiles/main_page.html')


class ProfileView(DetailView):
    model = Profile
    template_name = 'profiles/profile.html'
    
    def get_object(self, *args, **kwargs):
        return get_object_or_404(Profile, user=self.request.user)
    
    
class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profiles_list.html'
    context_object_name = 'profiles'
    
    def get_queryset(self):
        return Profile.objects.all()
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
    
