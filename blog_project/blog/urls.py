from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<int:id>', views.blog, name='blog'),
    path('category/<cat>', views.category, name='category'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('addpost/', views.add_post, name='addpost'),
    path('edit/<int:id>', views.blog_edit, name='edit'),
    path('delete/<int:id>', views.blog_delete, name='delete'),


]