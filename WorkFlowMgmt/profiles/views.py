from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.db.models import Q

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
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(user__first_name__iscontains=search_query) |
                Q(user__last_name__iscontains=search_query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_groups'] = [(profile, profile.user.groups.all()) for profile in context['profiles']]
        profiles = context['profiles']
        return context
    
    
