from django.shortcuts import render


# Create your views here.
def prescription(request):
    return render(request, 'backend/prescription/prescription.html')
