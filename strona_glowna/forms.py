from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import DaneWlasciwosciFizycznych


class FormularzLogowania(AuthenticationForm):
    """
    Log in form
    """
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Nazwa użytkownika'}),
        error_messages={
            'required': 'Pole nie może być puste!',
            'max_length': 'Wprowadź krótszą nazwę użytkownika (maksymalnie 30 znaków).'
        }
    )

    class Meta:
        model = User
        fields = ['username', 'password']


class FormularzRejestracji(UserCreationForm):
    """
    Register form
    """
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Nazwa użytkownika'}),
        error_messages={
            'required': 'Pole nie może być puste!',
            'max_length': 'Wprowadź krótszą nazwę użytkownika (maksymalnie 30 znaków).'
        }
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class DaneWlasciwosciFizycznychForm(forms.ModelForm):
    """
    Physical properties form - I am not sure if I am using it in this project, I have to check this
    """
    class Meta:
        model = DaneWlasciwosciFizycznych
        fields = ["Density"]
        labels = {
            "Density": "Podaj gęstość swojego materiału",
        }
