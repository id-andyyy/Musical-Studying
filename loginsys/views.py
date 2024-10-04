from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template.context_processors import csrf

from .forms import UserLoginForm, UserRegisterForm, UserInfoForm


def user_login(request):
    context = {'title': 'Вход'}
    context.update(csrf(request))
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
        else:
            form = UserLoginForm()
            messages.error(request, 'Пользователь не найден')
    else:
        form = UserLoginForm()
    context.update({'form': form})
    return render(request, 'loginsys/login_page.html', context)


def user_register(request):
    if request.method == 'POST':
        form_1 = UserRegisterForm(request.POST)
        form_2 = UserInfoForm(request.POST)
        if form_1.is_valid() and form_2.is_valid():
            form_1.save()
            user = authenticate(username=form_1.cleaned_data['username'], password=form_1.cleaned_data['password2'])
            login(request, user)
            form_2.instance.user = User.objects.get(pk=request.user.id)
            form_2.save()
            login(request, user)
            messages.success(request, 'Регистрация завершена')
            return redirect('main')
        else:
            messages.error(request, 'Ошибка регистрации!')
    else:
        form_1 = UserRegisterForm()
        form_2 = UserInfoForm(request.POST)
    return render(request, 'loginsys/register_page.html', {'title': 'Регистрация', 'form_1': form_1, 'form_2': form_2})


def user_logout(request):
    logout(request)
    return redirect('login')
