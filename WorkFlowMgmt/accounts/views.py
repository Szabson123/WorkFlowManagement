from django.shortcuts import render, redirect
from base.models import Profile
from base.forms import UserForm

from django.contrib.auth import login


def user_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST) 
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user) 
            login(request, user)  
            return redirect('profiles:main_page') 
    else:
        form = UserForm()  
    return render(request, 'accounts/register_user.html', {'form': form})
