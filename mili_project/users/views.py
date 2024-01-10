
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views.decorators.csrf import csrf_protect

from django.db import IntegrityError
# Create your views here.
# def login(request):
#     return render(request, 'users/login.html')

# def register(request):
#     return render(request, 'users/register.html')
# def profile(request):
#     users=User.objects.all()
#     profiles=Profile.objects.all()
#     context={
#         'users':users,
#         'profiles':profiles,
#     }
#     return render(request, 'users/profile.html')

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('bako_mili:index')  # Replace 'bako_mili:index' with your desired redirect URL
        else:
            messages.warning(request, 'Login failed. Try again.')
            return render(request, 'users/login.html', {'invalid_creds': True})
    return render(request, 'users/login.html')



@login_required
# def profile(request):
#     try:
#         user_profile = request.user.profile  # Access the user's profile
#     except ObjectDoesNotExist:
#         user_profile = None  # Handle the case where the profile doesn't exist
#     return render(request, 'users/profile.html', {'user_profile': user_profile})

def profile(request):
    try:
        user_profile = request.user.profile
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form,
            'user_profile': user_profile
        }
    except ObjectDoesNotExist:
        user_profile = None
        context = {
            'user_profile': user_profile
        }

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('user:profile')

    return render(request, 'users/profile.html', context)

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Your account has been created! You can now log in.')
                return redirect('user:login')
            except IntegrityError as e:
                form.add_error('email', 'This email is already in use.')  # Show error in the form
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})