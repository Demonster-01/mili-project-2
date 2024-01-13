
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Service, Net, Officer, Revenue, expense
from .forms import IncomeForm,ExpenseForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# import nepali_datetime
from django.contrib.auth.models import User
from .utils import get_plot
from .models import Revenue,expense
from django.contrib import messages

from django.db import models



# Create your views here.
def index(request):
    officers = Officer.objects.all()
    context = {
        'officers': officers,
    }
    return render(request, 'bako_mili/index.html', context)


def waterbill(request):
    water_services = Service.objects.filter(title='water')
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


@login_required()
def income(request):
    # qs=Revenue.objects.all()
    # x=[x.transaction_date for x in qs]
    # y=[y.amount for y in qs]
    # chart=get_plot(x,y)
    
    income_chart = Revenue.objects.all()
    x = [entry.transaction_date for entry in income_chart]
    y = [entry.amount for entry in income_chart]
    
    expense_chart = expense.objects.all()
    a = [entry.transaction_date for entry in expense_chart]
    b = [entry.amount for entry in expense_chart]
    
    if not x and not a:
        print("No data available.")
        x=0
        y=0
        a=0
        b=0
        chart = get_plot(x,y,a,b)
        
    else:
        data = list(zip(a, b))
        sorted_data = sorted(data, key=lambda entry: entry[0])
        sorted_a, sorted_b = zip(*sorted_data)

        data2 = list(zip(x, y))
        sorted_data2 = sorted(data2, key=lambda entry: entry[0])
        sorted_x, sorted_y = zip(*sorted_data2)

        chart = get_plot(sorted_a, sorted_b, sorted_x, sorted_y)
    
    
    user = request.user  # The logged-in user
    income_form = IncomeForm(request.POST, initial={'collector': user.username})
    expense_form = ExpenseForm(request.POST, request.FILES)
    total_collection = Revenue.objects.aggregate(total_collection=models.Sum('amount'))['total_collection']
    total_expense = expense.objects.aggregate(total_expense=models.Sum('amount'))['total_expense']


 
    context={
            'total_collection':total_collection,
            'total_expense':total_expense,
            'chart':chart,
            'income_form': income_form,
            'expense_form': expense_form
        }


    if request.method == 'POST':

        
        if income_form.is_valid():
            collector_name = income_form.cleaned_data.get('collector')
            revenue_instance = Revenue.objects.create(
                payer=income_form.cleaned_data.get('payer'),
                amount=income_form.cleaned_data.get('amount'),
                service=income_form.cleaned_data.get('service'),
                transaction_date=income_form.cleaned_data.get('transaction_date'),
                remark=income_form.cleaned_data.get('remark'),
                collector=collector_name
            )

            revenue_instance.save()

            return redirect('bako_mili:income')
        
        if expense_form.is_valid():
            amount = expense_form.cleaned_data['amount']
            image = expense_form.cleaned_data.get('image')
            title= expense_form.cleaned_data.get('title'),

            if amount > 500 and not image:
                messages.error(request, 'Image is required for amounts higher than 500.')
            else:  
                expense_instance = expense.objects.create(
                    title= expense_form.cleaned_data.get('title'),
                    amount=amount,
                    image=image,
                    remark=expense_form.cleaned_data.get('remark')
                )
                expense_instance.save()
                messages.success(request, 'Expense saved successfully.')
                return redirect('bako_mili:income')
    else:
        income_form = IncomeForm(initial={'collector': user.username, 'transaction_date': timezone.now()})
        expense_form = ExpenseForm(initial={'transaction_date': timezone.now()})
        
    context.update({'income_form': income_form, 'expense_form': expense_form})
    return render(request, 'bako_mili/plan.html',context)

def data(request):
    incomes = Revenue.objects.all().order_by('transaction_date')
    expenses = expense.objects.all().order_by('transaction_date')
    context = {
        'incomes': incomes,
        'expenses': expenses,
    }
    return render(request, 'bako_mili/data.html', context)
