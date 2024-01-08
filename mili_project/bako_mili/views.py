from django.shortcuts import render
from .models import Service

# Create your views here.
def index(request):
    return render(request, 'bako_mili/index.html')



def waterbill(request):
    water_services = Service.objects.filter(title='water')  # Assuming 'water' is a category for water services
    context = {
        'services': water_services,
    }
    return render(request, 'bako_mili/waterbill.html', context)

def garbagebill(request):
    garbage_services = Service.objects.filter(title='Garbage') 
    context = {
        'services': garbage_services,
    }
    return render(request, 'bako_mili/waterbill.html', context)

def netbill(request):
    garbage_services = Service.objects.filter(title='Garbage') 
    context = {
        'services': garbage_services,
    }
    return render(request, 'bako_mili/waterbill.html', context)