from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import BlogPostFrom
from django.contrib import messages
from .models import Blog
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


# Home
def home(request):
    all_blog = Blog.objects.all().order_by('-id')
    return render(request, 'blog/home.html', {'all_blog': all_blog})


# Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        blogs =  Blog.objects.filter(user=request.user).order_by('-id')
        context = {
                    'blogs':blogs,
                    'all_blog' : Blog.objects.all(),
                }
        return render(request, 'blog/dashboard.html', context)
    else:
        messages.warning(request, 'You must log in first.')
        return HttpResponseRedirect('/user/login/')


def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = BlogPostFrom(request.POST)
            if fm.is_valid():
                blog = fm.save(commit=False)
                blog.user = request.user
                blog.save()
                return HttpResponseRedirect('/dashboard/')

        else:
            fm = BlogPostFrom()
        context = {
                    'fm':fm,
                    'all_blog' : Blog.objects.all(),
                }
        return render(request, 'blog/addpost.html', context)
    else:
        return HttpResponseRedirect('/user/login/')


# Edit Blog 
def blog_edit(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Blog.objects.get(pk=id)
            fm = BlogPostFrom(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Successfully Update!')
                return HttpResponseRedirect('/dashboard/')

        else:
            pi = Blog.objects.get(pk=id)
            fm = BlogPostFrom(instance=pi)        
        context = {
                    'fm':fm,
                    'all_blog' : Blog.objects.all(),
                }
        return render(request, 'blog/edit.html', context)          
    else:
        return HttpResponseRedirect('/user/login/')


# Delete Blog
def blog_delete(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Blog.objects.get(pk=id)
            pi.delete()
            messages.success(request, 'Successfully Delete!')

        return HttpResponseRedirect('/dashboard/')          
    else:
        return HttpResponseRedirect('/user/login/')


# Blog
def blog(request, id):
    try:
        context = {
    'blog' : Blog.objects.get(pk=id),
    'all_blog' : Blog.objects.all(),
}
    except ObjectDoesNotExist:
            messages.warning(request, 'Blog Does Not Exist')
            return redirect('home')
    return render(request, 'blog/blog.html', context)


#Blog category's
def category(request, cat):
    context = {
        'category_blog' : Blog.objects.filter(category = cat),
        'all_blog' : Blog.objects.all(),
        'category' : cat
    }
    return render(request, 'blog/categoryblog.html', context)