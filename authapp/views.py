# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.files.images import get_image_dimensions
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.conf import settings
from django.http import HttpResponse, Http404
import os
import requests

VALID_COUNTRIES = ['US', 'FR', 'DE', 'ES', 'IT', 'GB', 'CA', 'AU', 'NZ', 'IN', 'BR']  # Example list

def register(request):
    if request.method == 'POST':
        # Form data
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        country = request.POST.get('country', '').strip().upper()
        city = request.POST.get('city', '').strip()
        birthdate = request.POST.get('birthdate', '')
        avatar = request.FILES.get('avatar')
        recaptcha_token = request.POST.get('recaptcha_token')

        form_data = {
            'username': username,
            'email': email,
            'country': country,
            'city': city,
            'birthdate': birthdate
        }

        # reCAPTCHA validation
        recaptcha_response = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': settings.RECAPTCHA_SECRET_KEY,
                'response': recaptcha_token
            }
        )
        recaptcha_result = recaptcha_response.json()

        if not recaptcha_result.get('success'):
            return render(request, 'authapp/register.html', {'error': 'Invalid reCAPTCHA. Please try again.', 'form_data': form_data})

        # Form validations
        if password1 != password2:
            return render(request, 'authapp/register.html', {'error': 'Passwords do not match.', 'form_data': form_data})
        if len(username) < 3 or len(username) > 30:
            return render(request, 'authapp/register.html', {'error': 'Username must be between 3 and 30 characters.', 'form_data': form_data})
        if User.objects.filter(username=username).exists():
            return render(request, 'authapp/register.html', {'error': 'Username is already taken.', 'form_data': form_data})
        if User.objects.filter(email=email).exists():
            return render(request, 'authapp/register.html', {'error': 'Email is already in use.', 'form_data': form_data})

        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'authapp/register.html', {'error': 'Invalid email address.', 'form_data': form_data})

        if country not in VALID_COUNTRIES:
            return render(request, 'authapp/register.html', {'error': 'Invalid country.', 'form_data': form_data})

        if avatar:
            try:
                width, height = get_image_dimensions(avatar)
                if avatar.size > 2 * 1024 * 1024:
                    return render(request, 'authapp/register.html', {'error': 'Avatar file size should be less than 2MB.', 'form_data': form_data})
                if width > 500 or height > 500:
                    return render(request, 'authapp/register.html', {'error': 'Avatar dimensions should be 500x500 pixels or less.', 'form_data': form_data})
            except Exception:
                return render(request, 'authapp/register.html', {'error': 'Invalid image file.', 'form_data': form_data})

        # Create user and profile
        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            profile = Profile(user=user, country=country, city=city, birthdate=birthdate, avatar=avatar)
            profile.save()
            login(request, user)
            return redirect('home')
        except ValidationError as e:
            return render(request, 'authapp/register.html', {'error': str(e), 'form_data': form_data})
        except Exception as e:
            return render(request, 'authapp/register.html', {'error': 'An error occurred while creating the profile. Please try again.', 'form_data': form_data})

    return render(request, 'authapp/register.html', {'recaptcha_site_key': settings.RECAPTCHA_SITE_KEY})

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'authapp/profile.html', {'profile': profile})

@login_required
def update_profile(request):
    if request.method == 'POST':
        user = request.user
        profile = Profile.objects.get(user=user)
        
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        country = request.POST.get('country', '').strip()
        city = request.POST.get('city', '').strip()
        birthdate = request.POST.get('birthdate', '')
        avatar = request.FILES.get('avatar')
        
        try:
            if User.objects.filter(username=username).exclude(pk=user.pk).exists():
                raise ValidationError('Username already taken.')
            if User.objects.filter(email=email).exclude(pk=user.pk).exists():
                raise ValidationError('Email already in use.')
            
            user.username = username
            user.email = email
            user.save()
            
            profile.country = country
            profile.city = city
            profile.birthdate = birthdate
            
            if avatar:
                width, height = get_image_dimensions(avatar)
                if avatar.size > 2 * 1024 * 1024:
                    raise ValidationError('Avatar file size should be less than 2MB.')
                if width > 500 or height > 500:
                    raise ValidationError('Avatar dimensions should be 500x500 pixels or less.')
                profile.avatar = avatar
            
            profile.save()
            return redirect(reverse('profile', kwargs={'username': user.username}))
        except ValidationError as e:
            return render(request, 'authapp/profile.html', {'profile': profile, 'error': str(e)})
    
    return redirect(reverse('profile', kwargs={'username': request.user.username}))

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('profile', kwargs={'username': user.username}))
        else:
            return render(request, 'authapp/login.html', {'error': 'Invalid username or password'})
    return render(request, 'authapp/login.html')
    
@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'authapp/profile.html', {'user': user, 'profile': profile})

def avatar_view(request, username):
    file_path = os.path.join(settings.MEDIA_ROOT, f'{username}.png')
    
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            return HttpResponse(f.read(), content_type="image/png")
    else:
        raise Http404("Avatar not found")

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})