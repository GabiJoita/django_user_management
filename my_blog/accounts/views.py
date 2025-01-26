from django.shortcuts import render
from .models import UserInfo


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
