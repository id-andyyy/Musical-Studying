from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Profiles


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'Логин',
    }))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'type': 'password',
        'class': 'form-control',
        'placeholder': 'Пароль',
    }))

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='', help_text='', min_length=4, max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Логин',
    }))
    password1 = forms.CharField(label='', help_text='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль',
    }))
    password2 = forms.CharField(label='', help_text='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Повторите пароль',
    }))
    email = forms.EmailField(label='', help_text='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'aria-describedby': 'emailHelp',
        'placeholder': 'Электронная почта',
    }))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


class UserInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['level'].empty_label = 'Уровень английского'
        self.fields['mode'].empty_label = 'Режим тренировки'

    class Meta:
        model = Profiles
        fields = ['user', 'age', 'level', 'mode', 'genres']
        widgets = {
            'user': forms.HiddenInput(),
            'age': forms.NumberInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Возраст',
            }),
            'level': forms.Select(attrs={
                'class': 'custom-select',
            }),
            'mode': forms.Select(attrs={
                'class': 'custom-select',
            }),
            'genres': forms.CheckboxSelectMultiple(attrs={
                'type': 'checkbox',
                # 'class': 'custom-control-input',
            }),
        }
