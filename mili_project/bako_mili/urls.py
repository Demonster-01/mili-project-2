
from django.urls import path
from .import views

app_name = 'bako_mili' 
urlpatterns = [
    path('',views.index,name="index"),
    # path('waterbill/', views.waterbill, name='mili-waterbill'),
    path('waterbill/',  views.waterbill, name='waterbill'),
    path('garbagebill/',  views.garbagebill, name='garbagebill'),
    path('netbill/',  views.netbill, name='netbill'),
    path('income/',  views.income, name='income'),
]
