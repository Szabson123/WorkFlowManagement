from django.urls import path
from django.contrib.auth.views import LoginView
from accounts.views import user_register

app_name = 'accounts'

urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', user_register, name='register'),
]
