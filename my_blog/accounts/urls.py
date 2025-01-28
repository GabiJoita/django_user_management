from django.urls import path
from .views import submit_info
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Route for index.html
    path('home/', views.home, name='home'),  # Route for home.html
]