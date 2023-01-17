from django.contrib import admin
from .models import Blog, ProfileUser
# Register your models here.

@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']

@admin.register(ProfileUser)
class ProfileUserModelAdmin(admin.ModelAdmin):
    list_display = ['user']    

