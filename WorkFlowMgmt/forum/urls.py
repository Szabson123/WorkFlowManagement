from django.urls import path
from forum.views import *

app_name = 'forum'

urlpatterns = [
    path('', MainForumPage.as_view(), name='forum_main_page')
]