from cgi import print_exception
from email.mime import image
from unicodedata import name
from django.db import models
from distutils.command.upload import upload
import importlib
from tkinter import CASCADE
from django.contrib.auth.models import User
from Register.models import*

# Create your models here.

class category(models.Model):
    category_name=models.CharField(max_length=250)
    category_description=models.TextField()
    category_image=models.ImageField(upload_to="media/SparePartsimage")
    category_updated_on=models.DateTimeField(auto_now=True)
    def ___str___(self):
        return self.category_name
    
    
class SpareParts(models.Model):
    cat=models.ForeignKey(category,on_delete=models.CASCADE,default=1)
    product= models.CharField(max_length=250)
    discription=models.TextField()
    price=models.IntegerField()
    updated_on=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="media/SparePartsimage")
    updated_on=models.DateTimeField(auto_now=True)
    
class cart(models.Model):
    cour=models.ForeignKey(SpareParts,on_delete=models.CASCADE)
    usr=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    status=models.BooleanField(default=False)
    add_on=models.DateTimeField(auto_now_add=True,null=True)
    updated_on=models.DateTimeField(auto_now=True,null=True)
    
class Order(models.Model):
    cust_id=models.ForeignKey(User, on_delete=models.CASCADE)
    cart_ids=models.CharField(max_length=150)
    product_ids=models.CharField(max_length=150)
    invoice_id=models.CharField(max_length=150)
    status=models.BooleanField(default=False)
    processed_on=models.DateTimeField(auto_now=True)

class feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    revbody=models.TextField()
    ratpro=models.ForeignKey(SpareParts,on_delete=models.CASCADE)
    addon=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username 

class contact(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=500)
    message=models.TextField()
    contnum=models.PositiveBigIntegerField()
    updated_on=models.DateTimeField(auto_now=True)


class whishlist(models.Model):
    product=models.ForeignKey(SpareParts,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    status=models.BooleanField(default=False)
    add_on=models.DateTimeField(auto_now_add=True,null=True)
    updated_on=models.DateTimeField(auto_now=True,null=True) 