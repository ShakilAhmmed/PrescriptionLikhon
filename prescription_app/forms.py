from django import forms
from .models import PrescriptionPatient


class PatientForm(forms.ModelForm):
    class Meta:
        model = PrescriptionPatient
        fields = "__all__"
        CHOICES = ((1,'Male'),(2,'Female'),(3,'Others'))
        widgets = {
            "patient_name" : forms.TextInput(attrs={"class":"form-control"}),
            "patient_age" : forms.NumberInput(attrs={"class":"form-control"}),
            "patient_sex" : forms.Select( choices=CHOICES,attrs={"class":"form-control"} ),
            "patient_phone" : forms.TextInput(attrs={"class":"form-control"}),
            "prescription_date" : forms.TextInput(attrs={"class":"form-control","type":"date"}),
        }
