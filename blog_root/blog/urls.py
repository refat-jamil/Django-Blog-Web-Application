from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('userprofile/', views.user_profile, name='userprofile'),
    path('profile/<int:id>', views.profile, name='profile'),

    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('addpost/', views.add_post, name='addpost'),
    path('edit/<int:id>', views.blog_edit, name='edit'),
    path('delete/<int:id>', views.blog_delete, name='delete'),


]