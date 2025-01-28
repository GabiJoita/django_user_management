# Import necessary modules
from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # <-- This import goes here
from django.contrib import messages
from django.contrib.auth import authenticate, login


# View for registering new users
def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
        else:
            # Create the user and hash the password
            User.objects.create_user(username=username, password=password)
            messages.success(request, "User registered successfully!")
        return redirect('index')

    return render(request, 'index.html')


# View for logging in users
def home(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Print the entered credentials for debugging
        print(f"Attempting to login with Username: {username} and Password: {password}")

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        # Check if user exists after authentication
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard if login is successful
        else:
            print(f"Authentication failed for username: {username}")
            return render(request, 'home.html', {'error_message': 'Invalid username or password!'})

    return render(request, 'home.html')


# Example view for dashboard
def dashboard(request):
    return render(request, 'dashboard.html')
