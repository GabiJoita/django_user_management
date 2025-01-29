from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserInfo


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

    return render(request, 'index.html')


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Try to find the user in the database
        user = UserInfo.objects.filter(username=username, password=password).first()

        if user:
            # If the user is found, login and redirect to a dashboard
            # Here, you can implement a custom login system if necessary
            return redirect('dashboard')  # Assuming you have a dashboard view

        else:
            return render(request, 'home.html', {'error_message': 'Invalid username or password'})

    return render(request, 'home.html')
