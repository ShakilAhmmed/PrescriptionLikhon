from django.db import models
from medicine_app.models import Medicine
# Create your models here.


class PrescriptionPatient(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_age = models.IntegerField()
    patient_sex = models.IntegerField()
    patient_phone = models.CharField(max_length=100)
    prescription_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PrescriptionMedicine(models.Model):
    prescription_patient = models.ForeignKey( PrescriptionPatient, on_delete = models.CASCADE)
    medicine = models.ForeignKey( Medicine , on_delete = models.CASCADE)
    duration = models.IntegerField()
    duration_type = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PrescriptionMedicineDuration(models.Model):
      prescription_patient = models.ForeignKey( PrescriptionPatient, on_delete = models.CASCADE)
      prescription_medicine = models.ForeignKey( PrescriptionMedicine, on_delete = models.CASCADE)
      medicine_duration = models.IntegerField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
