from django.shortcuts import redirect, render

from .forms import EditProfileForm
from .models import Profile
from django.shortcuts import render
from django.contrib.auth import *

def home1(request):
    return render(request,'index.html')

    
def update_profile(request, id):
    userID = Profile.objects.get(user_id=id)
    form = EditProfileForm(request.POST or None, instance=userID)
    if form.is_valid():
        form.save()
        return redirect('home')
    
    return render(request,'editP.html',
                  {'form': form})