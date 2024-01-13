from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))  # we can live EmailFirld(required=True) for true
    first_name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'UserName'}))
    house_no = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'House number'}))
    contact_no = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'Contact number'}))
    password1 = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['first_name','last_name','username','house_no','contact_no', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False  # Hide all labels in the form
        self.helper.add_input(Submit('submit', 'Sign Up'))
        
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.house_no = self.cleaned_data['house_no']
        user.contact_no = self.cleaned_data['contact_no']

        if commit:
            user.save()
            profile = Profile.objects.create(user=user)
            profile.house_no = user.house_no
            profile.contact = user.contact_no
            profile.save()

        return user


class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields=['username','email']
        
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False  # Hide all labels in the form
        self.helper.add_input(Submit('submit', 'Update'))

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['house_no','image']
        
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False  # Hide all labels in the form
        self.helper.add_input(Submit('submit', 'Update'))