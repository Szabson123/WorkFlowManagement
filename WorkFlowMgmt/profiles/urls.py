from django.urls import path
from profiles.views import main_page


app_name = 'profiles'

urlpatterns=[
    path('main_page/', main_page, name='main_page')
]

