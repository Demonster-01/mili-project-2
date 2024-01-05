from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100)
    monthly_rate=models.IntegerField(default=1)
    date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class net(models.Model):
    title = models.CharField(max_length=100)
    monthly_rate=models.IntegerField(default=1)
    plans=models.CharField(max_length=100)
    service= models.ForeignKey(Service,on_delete=models.DO_NOTHING)


class Revenue(models.Model):
    customer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING, related_name='service')
    transaction_date = models.DateField(default=timezone.now)
    remark=models.CharField(max_length=50)
    paid_from=models.CharField(max_length=10,default="Online")

    def __str__(self):
        return f"{self.customer.username} - {self.service.title}"