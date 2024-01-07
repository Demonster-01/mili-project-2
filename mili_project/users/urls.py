
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

app_name = 'user' 
urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('login/',  views.login, name='login'),
    path('register/',views.register,name="register"),

]