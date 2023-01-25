from django.contrib import admin
from .models import Blog, Profile
# Register your models here.

@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'category', 'create_at', 'update_at']

@admin.register(Profile)
class ProfileUserModelAdmin(admin.ModelAdmin):
    list_display = ['user']    

