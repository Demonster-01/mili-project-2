from django.contrib import admin

# Register your models here.
from .models import Service,Revenue,Net,Officer
# Register your models here.
admin.site.register(Service)
admin.site.register(Revenue)
admin.site.register(Net)
admin.site.register(Officer)