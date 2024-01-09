
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

from django.views.decorators.csrf import csrf_protect
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


@csrf_protect
# def register(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('firstname')
#         last_name = request.POST.get('lastname')
#         email = request.POST.get('email')
#         house_no = request.POST.get('house_no')
#         password = request.POST.get('password')
#         password2 = request.POST.get('password2')

#         # Basic validation
#         if not (first_name and last_name and email and house_no and password and password2):
#             messages.warning(request, 'Please fill in all fields.')
#             return render(request, 'users/register.html', {'invalid_creds': True})

#         if password != password2:
#             messages.warning(request, 'Passwords do not match.')
#             return render(request, 'users/register.html', {'invalid_creds': True})

#         if User.objects.filter(email=email).exists():
#             messages.warning(request, 'This email is already registered.')
#             return render(request, 'users/register.html', {'invalid_creds': True})

#         # Create a new user
#         user = User.objects.create_user(
#             email=email,
#             username=email,
#             password=password
#         )
#         user.first_name = first_name
#         user.last_name = last_name

#         user.save()
#         # Create a new profile
#         profile = Profile(user=user, house_no=house_no)
#         profile.save()

#         messages.success(request, 'Registration successful. You can now login.')
#         return HttpResponseRedirect(reverse('user:login')) # Redirect to login page or any other page

#     return render(request, 'users/register.html')



# @login_required
# def profile(request):
#     if request.user.is_authenticated:
#         profile = Profile.objects.get(user=request.user)
#         return render(request, 'users/profile.html', {'profile': profile, 'user': request.user})
#     else:
#         return redirect('login')


def profile(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        return render(request, 'profile.html', {'profile': profile, 'user': request.user})
    else:
        return redirect('login')
    
    


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})