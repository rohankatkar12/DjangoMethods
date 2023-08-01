from django.urls import path
from . import views

urlpatterns = [
    path('', views.receipes, name="reciepes")
]
