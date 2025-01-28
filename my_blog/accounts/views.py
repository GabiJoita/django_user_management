from .models import UserInfo
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


def submit_info(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Save to database
        UserInfo.objects.create(username=username, password=password)
        # Prepare the welcome message
        message = f"Welcome, {username}!"

    return render(request, 'index.html', {'message': message})


def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "User registered successfully!")
        return redirect('index')

    return render(request, 'index.html')


def home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Replace 'dashboard' with your actual route after login
        else:
            return render(request, 'home.html', {'error_message': 'Invalid credentials!'})

    return render(request, 'home.html')
