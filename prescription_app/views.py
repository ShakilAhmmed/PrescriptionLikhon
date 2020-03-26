from django.shortcuts import render

from .forms import PatientForm
# Create your views here.
def prescription(request):
    form = PatientForm()
    if request.method == "POST":
        print(request.POST)
    context = {
        "patient_form" : PatientForm
    }
    return render(request, 'backend/prescription/prescription.html',context)
