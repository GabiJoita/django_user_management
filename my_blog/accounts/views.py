# Import necessary modules
from django.shortcuts import render, redirect
from .models import UserInfo  # <-- This import goes here
from django.contrib import messages
from django.contrib.auth import authenticate, login


# View for registering new users

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username already exists
        if UserInfo.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
        else:
            # Save the new user
            new_user = UserInfo(username=username, password=password)
            new_user.save()
            messages.success(request, "Registration successful!")
            return redirect('home')  # Redirect to home page

    return render(request, 'index.html')  # Render the index page


# View for logging in users

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login the user and redirect to the dashboard (or another page)
            login(request, user)
            return redirect('dashboard')  # Redirect to the next page
        else:
            # If credentials are wrong, show an error message
            return render(request, 'home.html', {'error_message': 'Invalid username or password'})

    return render(request, 'home.html')

# Example view for dashboard
def dashboard(request):
    return render(request, 'dashboard.html')
