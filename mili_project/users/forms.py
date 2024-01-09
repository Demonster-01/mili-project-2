from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))  # we can live EmailFirld(required=True) for true
    First_name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    Last_name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'UserName'}))
    password1 = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['First_name','Last_name','username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_labels = False  # Hide all labels in the form
        
        self.helper.add_input(Submit('submit', 'Sign Up'))


class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']