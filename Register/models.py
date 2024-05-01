from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class prof(models.Model):
    usr=models.ForeignKey(User,on_delete=models.CASCADE)
    img_pro=models.ImageField(upload_to="media",default="default\\default_imgpro.jpg")
    state=models.CharField(max_length=250,default="Not Available")
    city=models.CharField(max_length=250,default="Not Available")
    street=models.CharField(max_length=250,default="Not Available")
    ph_pro=models.BigIntegerField(default="196878558")
    updated_on=models.DateTimeField(auto_now_add=True)
 
    