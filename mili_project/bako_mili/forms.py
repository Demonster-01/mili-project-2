from django import forms
from .models import Revenue,Officer,Service,expense

from django.contrib.auth.models import User

class IncomeForm(forms.ModelForm):
    payer = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'placeholder': 'Payer'}))
    amount = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder': 'amount'}))
    service = forms.ModelChoiceField(queryset=Service.objects.all(), widget=forms.Select(attrs={'placeholder': 'service'}))
    remark = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'remark'}))
    collector = forms.CharField()

    class Meta:
        model = Revenue
        fields = ['payer', 'amount', 'service', 'transaction_date', 'remark','collector']
        
    collector = forms.CharField(disabled=True) 
    def __init__(self, *args, **kwargs):
            super(IncomeForm, self).__init__(*args, **kwargs)
            self.fields['payer'].queryset = User.objects.all()
            self.fields['service'].queryset = Service.objects.all()



class ExpenseForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    amount = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder': 'amount'}))
    remark = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'remark'}))
    # image = forms.ImageField(required=False) 
    image = forms.ImageField() 

    class Meta:
        model = expense
        fields = ['title', 'amount', 'image', 'transaction_date', 'remark']
