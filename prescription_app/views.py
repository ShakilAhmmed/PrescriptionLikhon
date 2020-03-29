from django.shortcuts import render, get_object_or_404
from .forms import PatientForm
from .models import PrescriptionMedicine
from medicine_app.models import Medicine
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
# Create your views here.
def prescription(request):
    all_medicine_list = Medicine.objects.all()
    patient_form = PatientForm()
    if request.method == "POST":
        patient_form = PatientForm(request.POST)
        if patient_form.is_valid():
            patient_form = patient_form.save()

            # Multiple Data
            all_medicine_name = request.POST.getlist("medicine_name[]")
            all_remarks = request.POST.getlist("remarks[]")
            all_schedule_is_morning = request.POST.getlist("schedule_is_morning[]")
            all_schedule_is_after_noon = request.POST.getlist("schedule_is_after_noon[]")
            all_schedule_is_night = request.POST.getlist("schedule_is_night[]")
            all_duration = request.POST.getlist("duration[]")
            all_duration_type = request.POST.getlist("duration_type[]")
            medicine_data = []
            for medicine_counter in range(len(all_medicine_name)):
                medicine_get = get_object_or_404(Medicine, pk=all_medicine_name[medicine_counter])
                medicine_object = PrescriptionMedicine()
                medicine_object.prescription_patient = patient_form
                medicine_object.medicine = medicine_get
                medicine_object.remarks  = all_remarks[medicine_counter]
                medicine_object.schedule_is_morning  = all_schedule_is_morning[medicine_counter]
                medicine_object.schedule_is_after_noon  = all_schedule_is_after_noon[medicine_counter]
                medicine_object.schedule_is_night  = all_schedule_is_night[medicine_counter]
                medicine_object.duration  = all_duration[medicine_counter]
                medicine_object.duration_type  = all_duration_type[medicine_counter]
                medicine_data.append(medicine_object)
            PrescriptionMedicine.objects.bulk_create(medicine_data)
            messages.success(request,"Prescription Created Successfully")
            return HttpResponseRedirect(reverse("prescription:prescription"))
    context = {
        "patient_form" : patient_form ,
        'all_medicine_list' : all_medicine_list
    }
    return render(request, 'backend/prescription/prescription.html',context)
