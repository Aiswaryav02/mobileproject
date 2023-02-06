from django.db import models
from account.models import User
from store.models import Products


# Create your models here.
class Purchase(models.Model):
        product=models.ForeignKey(Products,on_delete=models.CASCADE,related_name="product")
        user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
        date=models.DateField(null=True,auto_now_add=True)
        status=models.BooleanField(default=False)
        quantity=models.IntegerField(default='0')


class MyOrders(models.Model):
        product=models.ForeignKey(Products,on_delete=models.CASCADE,related_name="item")
        user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user1")
        date=models.DateField(null=True,auto_now_add=True)
        status=models.BooleanField(default=False)

class FeedbackModel(models.Model):
      date=models.DateField(null=True,auto_now_add=True)
      feedback=models.TextField()
      user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='userfb')
      product=models.ForeignKey(Products,on_delete=models.CASCADE,related_name="item1")
      






    