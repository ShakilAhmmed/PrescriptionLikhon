from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib import messages
import requests
from bs4 import BeautifulSoup
from .models import Medicine
from time import sleep


# Create your views here.
def pull_medicine(request):
    medicine_data = Medicine.objects.all()
    medicine_list = list(medicine_data.values_list("medicine_name", flat=True))

    paginator = Paginator(medicine_data, 10)
    page_number = request.GET.get('page')
    medicine_data = paginator.get_page(page_number)

    if request.method == "POST":
        # url = "http://www.squarepharma.com.bd/products-by-tradename.php?type=pharma&char=A"
        alpha = 'A'
        page_list = []
        for i in range(0, 26):
            page_list.append(alpha)
            alpha = chr(ord(alpha) + 1)
        data = []
        try:
            for page in page_list:
                url = f"http://www.squarepharma.com.bd/products-by-tradename.php?type=pharma&char={page}"
                print(f"Pulling From {url}")
                response = requests.get(url, verify=False, timeout=30)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, "html.parser")
                    all_medicine_div = soup.find_all("div", {"class": "pthumb"})
                    for medicine_data in all_medicine_div:
                        medicine_details_div = medicine_data.find("div", {
                            "class": "col-xs-6 col-sm-12 col-md-6 col-lg-6 sm-mid row-no-padding-left"})
                        medicine_name = medicine_details_div.find("h3").text if medicine_details_div.find("h3") else ''
                        medicine_generic_name = medicine_details_div.find("h4").text if medicine_details_div.find(
                            "h4") else ''
                        # data = [Medicine(medicine_name=medicine_name, medicine_generic_name=medicine_generic_name)]
                        if medicine_name not in medicine_list:
                            medicine = Medicine()
                            medicine.medicine_name = medicine_name
                            medicine.medicine_generic_name = medicine_generic_name
                            data.append(medicine)
            Medicine.objects.bulk_create(data)
            messages.success(request, "Successfully Medicine Pulled")
        except Exception as e:
            messages.error(request, f"An error {e}")
        context = {
            'medicine_data': medicine_data
        }
    else:
        context = {
            'medicine_data': medicine_data
        }
    return render(request, "backend/medicine/pull_medicine.html", context)
