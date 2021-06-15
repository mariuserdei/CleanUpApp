from django.urls import path
from .views import cities_list

urlpatterns = [
    path('cities/', cities_list)
]
