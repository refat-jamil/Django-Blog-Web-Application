from django.shortcuts import render, HttpResponseRedirect
from .forms import SingUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Blog
# Create your views here.

# Home
def home(request):
    all_blog = Blog.objects.all()
    return render(request, 'blog/home.html', {'all_blog': all_blog})


# About
def about(request):
    return render(request, 'blog/about.html')


# SingUp
def user_signup(request):
    if request.method == "POST":
        fm = SingUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Congratulation!! You have become a Author. Please Login.')
            fm.save()
    else:    
        fm = SingUpForm()
    return render(request, 'blog/signup.html', {'form':fm})     


# LogIn
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username= uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !')
                    return HttpResponseRedirect('/dashboard/')
        else:            
            fm = LoginForm()
        return render(request, 'blog/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')        

    
# Dashboard
def dashboard(request):
    return render(request, 'blog/dashboard.html')  

 
# LogOut
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')