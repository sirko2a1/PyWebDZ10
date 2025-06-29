from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Quote


def start_page(request):
    quotes = Quote.objects.prefetch_related('tags').all()
    return render(request, 'start_page.html', {'quotes': quotes})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  
            user.save()
            login(request, user)
            return redirect('start')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('start')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def confirm_logout_view(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        user = authenticate(username=request.user.username, password=password)
        if user:
            logout(request)
            return redirect('start')
        else:
            messages.error(request, "Wrong password. Try again.")
    return render(request, 'logout.html')