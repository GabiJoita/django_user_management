from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Route for index.html
    path('home/', views.home, name='home'),  # Route for home.html
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard after successful login
]