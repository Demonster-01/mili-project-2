from django.contrib import admin

# Register your models here.
from .models import Service,Revenue
# Register your models here.
# admin.site.unregister(Movie)
admin.site.register(Service)
admin.site.register(Revenue)