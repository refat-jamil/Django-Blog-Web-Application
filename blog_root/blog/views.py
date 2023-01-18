from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import SingUpForm, LoginForm, BlogPostFrom, UserProfileUpdateForm, UserImgUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Blog
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

# Home
def home(request):
    all_blog = Blog.objects.all()
    return render(request, 'blog/home.html', {'all_blog': all_blog})


# User Profile
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            p_form = UserProfileUpdateForm(request.POST, instance=request.user)
            i_form = UserImgUpdateForm(request.POST, request.FILES, instance=request.user.profile)
            if p_form.is_valid() and i_form.is_valid():
                p_form.save()
                i_form.save()
                messages.success(request, 'Successfully Update!')
                return redirect('userprofile')
        else:
            p_form = UserProfileUpdateForm(instance=request.user)
            i_form = UserImgUpdateForm()

        context = {
            'p_form':p_form,
            'i_form':i_form
        }
        return render(request, 'blog/userprofile.html', context)
    else:
        messages.warning(request, 'You must log in first.')
        return HttpResponseRedirect('/login/')

    


# SingUp
def user_signup(request):
    if request.method == "POST":
        fm = SingUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Congratulation!! You have become a Author. Please Login.')
            user = fm.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
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
    if request.user.is_authenticated:
        blogs = {'blog' : Blog.objects.all()}
        for i in blogs['blog']:
            print(type(i.user_id))
            if request.user.id == i.user_id:
                context = {'blogs':Blog.objects.filter(user_id = request.user.id)}
            else:    
                context = {'blogs':Blog.objects.filter(user_id = request.user.id)}

        return render(request, 'blog/dashboard.html', context)
    else:
        messages.warning(request, 'You must log in first.')
        return HttpResponseRedirect('/login/')

 
# LogOut
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')



def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = BlogPostFrom(request.POST)
            if fm.is_valid():
                blog = fm.save(commit=False)
                blog.user = request.user
                blog.save()
                return HttpResponseRedirect('/')

        else:
            fm = BlogPostFrom()
        return render(request, 'blog/addpost.html', {'fm':fm})
    else:
        return HttpResponseRedirect('/login/')



def blog_edit(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Blog.objects.get(pk=id)
            fm = BlogPostFrom(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Successfully Update!')
                return HttpResponseRedirect('/')

        else:
            pi = Blog.objects.get(pk=id)
            fm = BlogPostFrom(instance=pi)        

        return render(request, 'blog/edit.html', {'fm':fm})          
    else:
        return HttpResponseRedirect('/login/')



def blog_delete(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Blog.objects.get(pk=id)
            pi.delete()
            messages.success(request, 'Successfully Delete!')

        return HttpResponseRedirect('/dashboard/')          
    else:
        return HttpResponseRedirect('/login/')

