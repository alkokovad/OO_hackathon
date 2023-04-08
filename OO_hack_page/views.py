from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', { 'form': form})

def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('posts')
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('posts')

        # form is not valid or user is not authenticated
        messages.error(request, f'Invalid username or password')
        return render(request, 'users/login.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('login')
