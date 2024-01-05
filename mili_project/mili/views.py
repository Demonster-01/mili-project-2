from django.shortcuts import render
from .models import Service

# Create your views here.
def index(request):
    return render(request, 'mili/index.html')

# def waterbill(request):
#     services = Service.objects.all()  # Retrieve all services
#     context = {
#         'services': services,  # Use the plural form in the context
#     }
#     return render(request, 'mili/waterbill.html', context)

def waterbill(request):
    water_services = Service.objects.filter(title='water')  # Assuming 'water' is a category for water services
    context = {
        'services': water_services,
    }
    return render(request, 'mili/waterbill.html', context)

def garbagebill(request):
    garbage_services = Service.objects.filter(title='Garbage') 
    context = {
        'services': garbage_services,
    }
    return render(request, 'mili/waterbill.html', context)

def netbill(request):
    garbage_services = Service.objects.filter(title='Garbage') 
    context = {
        'services': garbage_services,
    }
    return render(request, 'mili/waterbill.html', context)