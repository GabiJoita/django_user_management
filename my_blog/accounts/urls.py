from django.urls import path
from .views import submit_info

urlpatterns = [
    path('', submit_info, name='submit_info'),
]