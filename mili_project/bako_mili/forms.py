from django import forms
from .models import Revenue,Officer,Service

from django.contrib.auth.models import User
class IncomeForm(forms.ModelForm):
    payer = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'placeholder': 'Payer'}))
    amount = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder': 'amount'}))
    service = forms.ModelChoiceField(queryset=Service.objects.all(), widget=forms.Select(attrs={'placeholder': 'service'}))
    remark = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'remark'}))
    # collector_dropdown = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'placeholder': 'collector'}))
    collector = forms.CharField()

    class Meta:
        model = Revenue
        fields = ['payer', 'amount', 'service', 'transaction_date', 'remark','collector']
        
    collector = forms.CharField(disabled=True) 
    def __init__(self, *args, **kwargs):
            super(IncomeForm, self).__init__(*args, **kwargs)
            # Customize form fields, if needed
            self.fields['payer'].queryset = User.objects.all()
            self.fields['service'].queryset = Service.objects.all()



# class IncomeForm(forms.ModelForm):
#     customer = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'customer'}))
#     amount = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder': 'amount'}))
#     service = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'service'}))
#     remark = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'remark'}))
#     collector = forms.ModelChoiceField(queryset=User.objects.none(), widget=forms.HiddenInput())

#     class Meta:
#         model = Revenue
#         fields = ['customer', 'amount', 'service', 'transaction_date', 'remark']
