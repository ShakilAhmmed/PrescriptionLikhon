from django.urls import path
from . import views

urlpatterns = [
    path("", views.pull_medicine, name="pull_medicine")
]
