from django.shortcuts import render
from django.http import HttpResponseRedirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/posts/home')
    else:
        if request.method =='POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                homeurl = reverse("home")
                return HttpResponseRedirect(homeurl)
        else:
            form = RegisterForm()
        return render(request, 'accounts/register.html', {'form':form})

def auth_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/posts/home')
    else:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                #print(user.is_superuser()) #check it is superuser
                if user is not None:
                    login(request, user)
                    homeurl = reverse('home')
                    return HttpResponseRedirect(homeurl)
        else:
            form = LoginForm()
        return render(request, 'accounts/login.html', {'form':form})
    
def auth_logout(request):
    logout(request) #this will delete session
    return HttpResponseRedirect('/accounts/login')