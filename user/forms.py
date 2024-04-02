from django import forms
from django.forms import DateInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

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

class EditUser(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'birthdate']
        widgets = {
            'birthdate': DateInput(attrs={'type': 'date'}),
        }