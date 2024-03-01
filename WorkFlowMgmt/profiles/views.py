from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from base.models import Profile


def main_page(request):
    return render(request, 'profiles/main_page.html')


class ProfileView(DetailView):
    model = Profile
    template_name = 'profiles/profile.html'
    
    def get_object(self,):
        return get_object_or_404(Profile, user=self.request.user)
