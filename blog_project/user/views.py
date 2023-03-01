from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import SingUpForm, LoginForm, UserProfileUpdateForm, UserImgUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog.models import Blog
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


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
    context = {
                    'form':fm,
                    'all_blog' : Blog.objects.all(),
                }
    return render(request, 'user/signup.html', context)     



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
        context = {
                    'form':fm,
                    'all_blog' : Blog.objects.all(),
                }
        return render(request, 'user/login.html', context)
    else:
        return HttpResponseRedirect('/dashboard/')


# LogOut
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')        



# view, edite Own User Profile
def user_profile(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            p_form = UserProfileUpdateForm(request.POST, instance=request.user)
            i_form = UserImgUpdateForm(request.POST, request.FILES, instance=request.user.profile)
            if p_form.is_valid() and i_form.is_valid():
                p_form.save()
                i_form.save()
                messages.success(request, 'Successfully Update!')
                return redirect('userprofile', id=id)
        else:
            p_form = UserProfileUpdateForm(instance=request.user)
            i_form = UserImgUpdateForm()

        context = {
            'p_form':p_form,
            'i_form':i_form,
            'all_blog' : Blog.objects.all(),
            'user_blog' : Blog.objects.filter(user=id).order_by('-id'),

        }
        return render(request, 'user/userprofile.html', context)
    else:
        messages.warning(request, 'You must log in first.')
        return HttpResponseRedirect('/login/')


    
# view all user Profile
def profile(request, id):
    if id == 1:
        messages.warning(request, 'User Does Not Exist')
        return redirect('home')
    else:
        try:
            if id == request.user.id:
                return redirect('userprofile', id=id)
            else:    
                context = {
                    'user' : User.objects.get(pk=id),
                    'all_blog' : Blog.objects.all(),
                    'user_blog' : Blog.objects.filter(user=id).order_by('-id')
                }
        except ObjectDoesNotExist:
            messages.warning(request, 'User Does Not Exist')
            return redirect('home')
    return render(request, 'user/profile.html',context)    