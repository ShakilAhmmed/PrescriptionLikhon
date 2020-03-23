from django.urls import path
from . import views
app_name = "prescription"
urlpatterns = [
    path('', views.prescription, name="prescription")
]
