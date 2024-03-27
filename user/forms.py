from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class CustomSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'password': forms.CharField(widget=forms.PasswordInput),
            'password2': forms.CharField(widget=forms.PasswordInput)
        }
        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                return forms.ValidationError('Las contrasenias no coinciden')
            return cd['password2']