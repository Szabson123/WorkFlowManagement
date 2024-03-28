from django.urls import path
from forum.views import *

app_name = 'forum'

urlpatterns = [
    path('', MainForumPage.as_view(), name='forum'),
    path('new_post/', CreatePostView.as_view(), name='new_post')
]