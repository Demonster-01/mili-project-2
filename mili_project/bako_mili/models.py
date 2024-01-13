from django.db import models
from PIL import Image
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100)
    monthly_rate=models.IntegerField(default=1)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    class Meta:
        app_label = 'bako_mili'
    

class Net(models.Model):
    title = models.CharField(max_length=100)
    monthly_rate=models.IntegerField(default=1)
    speed=models.CharField(max_length=10)

    def __str__(self):
        return self.title

class Revenue(models.Model):
    payer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING, related_name='service')
    transaction_date = models.DateField(default=timezone.now())
    remark = models.CharField(max_length=50)
    collector = models.CharField(max_length=50,default="Bs")
    
    def __str__(self):
        return f"{self.payer.username} - {self.service.title}"

class expense(models.Model):
    title=models.CharField(max_length=30)
    amount= models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField(default=timezone.now())
    remark = models.CharField(max_length=50,null=True)
    # image = models.ImageField(upload_to='expense_bill_pics',null=True)
    image = models.ImageField(upload_to='expense_bill_pics/', blank=True, null=True)
  
    
    def __str__(self):
        return 'Rs. {:.2f} - Date: {}'.format(self.amount, self.transaction_date)
    
class Officer(models.Model):
    name= models.CharField(max_length=50)
    role= models.CharField(max_length=20)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def save(self, *args, **kwargs):
        super(Officer, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)