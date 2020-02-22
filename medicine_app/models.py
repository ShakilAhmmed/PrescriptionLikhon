from django.db import models


# Create your models here.
class Medicine(models.Model):
    medicine_name = models.CharField(max_length=100, unique=True)
    medicine_generic_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
