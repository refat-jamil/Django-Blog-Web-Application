from django.urls import path
from . import views

urlpatterns = [

    path('userprofile/<int:id>', views.user_profile, name='userprofile'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),




]