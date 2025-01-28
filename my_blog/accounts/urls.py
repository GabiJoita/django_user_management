from django.urls import path
from .views import submit_info
from . import views

urlpatterns = [
    path('', submit_info, name='submit_info'),
    path('home/', views.home, name='home'),
]