from django.urls import path
from profiles.views import ProfileView, ProfileListView, main_page


app_name = 'profiles'

urlpatterns=[
    path('main_page/', main_page, name='main_page'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profiles_list/', ProfileListView.as_view(), name='profiles_list')
]

