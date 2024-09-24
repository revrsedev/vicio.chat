# authapp/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('profile/', views.profile_view, name='profile'),  # This should match the view function name
    path('login/', views.login_view, name='login'), 
    path('password_change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('auth/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('avatars/<str:username>/', views.avatar_view, name='avatar'),  
]
