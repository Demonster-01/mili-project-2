
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="mili-index"),
    # path('waterbill/', views.waterbill, name='mili-waterbill'),
    path('waterbill/',  views.waterbill, name='waterbill'),
    path('garbagebill/',  views.garbagebill, name='garbagebill'),
    path('netbill/',  views.netbill, name='netbill'),
]
