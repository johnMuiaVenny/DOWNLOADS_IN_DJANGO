from django.urls import path
from .views import *
from . import views

app_name = "FILES"

urlpatterns = [
    path('', Home, name="Home"),
]