from django.urls import path
from forum.views import *

app_name = 'forum'

urlpatterns = [
    path('', MainForumPage.as_view(), name='forum'),
    path('new_post/', CreatePostView.as_view(), name='new_post'),
    path('my_posts/', MyPostsListView.as_view(), name='my_posts'),
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]