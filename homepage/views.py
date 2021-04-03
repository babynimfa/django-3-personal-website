from django.shortcuts import render, redirect
from .models import Project
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.forms import EmailField
from django.utils.translation import ugettext_lazy as _
from .forms import CreateUserForm


def home(request):
    projects = Project.objects.all()
    return render(request, 'homepage/home.html', {'projects':projects})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'homepage/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'homepage/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and Password did not match'})
        else:
            login(request, user)
            return redirect('home')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('loginuser')



#For SignUp Code

def signupuser(request):
    form = CreateUserForm()
    context = {'form':form}

    if request.method == 'GET':
        return render(request, 'homepage/signupuser.html', context)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], email =request.POST['email'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'homepage/signupuser.html', {'form':CreateUserForm(), 'error':'- Username has already been taken'})
        else:
            return render(request, 'homepage/signupuser.html', {'form':CreateUserForm(), 'error':'- Passwords did not match'})

#End of SignUp Codes
