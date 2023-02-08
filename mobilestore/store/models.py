from django.db import models
from account.models import User
# Create your models here.
class Products(models.Model):
    productname=models.CharField(max_length=120)
    productmodel=models.CharField(max_length=120)
    description=models.CharField(max_length=120)
    color=models.CharField(max_length=120)
    price=models.IntegerField()
    quantity=models.IntegerField()
    prodimg=models.ImageField(upload_to="productimg",null=True)
    store=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="storeuser")

   