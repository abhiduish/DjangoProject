from django.db import models
from django.db.models import Model 
from django.utils import timezone
# Create your models here.
class Customer(Model):   
    name = models.CharField(max_length=100)    
    account_no = models.IntegerField(default=0)    
    gender = models.CharField(max_length=10)    
    balance = models.FloatField(default=0.0)    
    address = models.CharField(max_length=100)    
    pub_date = models.DateTimeField('date published',default=timezone.now())


    def __str__(self):
        return "{0},{1},{2},{3},{4},{5}".format(self.name,self.account_no,self.gender,self.balance,self.address,self.pub_date)


