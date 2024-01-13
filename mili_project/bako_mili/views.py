
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Service, Net, Officer, Revenue
from .forms import IncomeForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from .utils import get_plot

# Create your views here.
def index(request):
    officers = Officer.objects.all()  # Note the change in variable names
    context = {
        'officers': officers,
    }
    return render(request, 'bako_mili/index.html', context)


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
    nets = Net.objects.all()
    context = {
        'nets': nets,
    }
    return render(request, 'bako_mili/netbill.html', context)


# def income(request):
#     # form = IncomeForm()
#     user = request.user  # The logged-in user
#     form = IncomeForm(initial={'collector': user})  # Pass the username as initial data

#     if request.method == 'POST':
#         form = IncomeForm(request.POST)
#         if form.is_valid():
#             # Get the User instance for the provided username (collector)
#             collector_name = form.cleaned_data.get('collector')
#             collector_user = User.objects.get(username=collector_name)

#             # Create a new Revenue instance
#             revenue_instance = Revenue.objects.create(
#                 customer=collector_user,  # Assign the User instance to the ForeignKey field
#                 amount=form.cleaned_data.get('amount'),
#                 service=form.cleaned_data.get('service'),
#                 transaction_date=form.cleaned_data.get('transaction_date'),
#                 remark=form.cleaned_data.get('remark'),
#                 collector=collector_user
#             )

#             # Save the Revenue instance
#             revenue_instance.save()

#             return redirect('bako_mili:index')

#     return render(request, 'bako_mili/plan.html', {'form': form})


@login_required()
def income(request):
    qs=Revenue.objects.all()
    x=[x.transaction_date for x in qs]
    y=[y.amount for y in qs]
    chart=get_plot(x,y)





    user = request.user  # The logged-in user

    if request.method == 'POST':
        form = IncomeForm(request.POST, initial={'collector': user.username})
        if form.is_valid():
            # Get the User instance for the provided username (collector)
            collector_name = form.cleaned_data.get('collector')
            # collector_user = User.objects.get(username=collector_name)

            # Create a new Revenue instance
            revenue_instance = Revenue.objects.create(
                # payer=collector_user,  # Assign the User instance to the ForeignKey field
                payer=form.cleaned_data.get('payer'),
                amount=form.cleaned_data.get('amount'),
                service=form.cleaned_data.get('service'),
                transaction_date=form.cleaned_data.get('transaction_date'),
                remark=form.cleaned_data.get('remark'),
                collector=collector_name
            )

            # Save the Revenue instance
            revenue_instance.save()

            return redirect('bako_mili:income')
    else:
        form = IncomeForm(initial={'collector': user.username, 'transaction_date': timezone.now()})

    return render(request, 'bako_mili/plan.html', {'form': form,'chart':chart})
