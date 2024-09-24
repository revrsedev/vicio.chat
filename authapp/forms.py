# authapp/forms.py

from django import forms
from .models import User
import requests
from django.conf import settings

class RegisterForm(forms.ModelForm):
    recaptcha_token = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        recaptcha_token = cleaned_data.get('recaptcha_token')

        if recaptcha_token:
            recaptcha_response = requests.post(
                'https://www.google.com/recaptcha/api/siteverify',
                data={
                    'secret': settings.RECAPTCHA_SECRET_KEY,
                    'response': recaptcha_token
                }
            )
            recaptcha_result = recaptcha_response.json()
            if not recaptcha_result.get('success'):
                raise forms.ValidationError('Invalid reCAPTCHA. Please try again.')
        else:
            raise forms.ValidationError('reCAPTCHA validation failed. Please try again.')
        
        return cleaned_data
