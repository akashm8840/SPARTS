from sre_parse import CATEGORIES
from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import *
from  Home.models import *
# Create your views here.
def register(request):
    if request.method=="POST":
        fn=request.POST["fn"]
        ln=request.POST["ln"]
        un=request.POST["uname"]
        em=request.POST["email"]
        pwdd=request.POST['pwd']
        cpw=request.POST['cpwd'] 
        phn=request.POST['phn']
        if(pwdd==cpw):
            usr=User.objects.create_user(username=un,first_name=fn,last_name=ln,email=em,password=pwdd)      
            usr.save()
            prf=prof(usr=usr,ph_pro=phn)
            prf.save()
        return redirect("login")
   
        
    return render(request,"registration.html")
def login(request):
    if request.method=="POST":
        un=request.POST["unm"]
        pwd=request.POST["pwd"]
        
        usrlog=auth.authenticate(username=un,password=pwd)
        if usrlog !=None :
            auth.login( request,usrlog)
            return redirect("ind")
        else:
            return redirect("log")
    return render(request,"login.html")        

def logout(request):
    auth.logout(request)
    return redirect("ind")

def Profile(request):
    dis={}
    pro=prof.objects.filter(usr__id=request.user.id)
    if len(pro)>0:
        prf=prof.objects.get(usr__id=request.user.id)
        dis['pro']=prf
    return render(request,'profile.html',dis)
def uppro(request):
    display={}
    prf=prof.objects.filter(usr__id=request.user.id)
    if len(prf)>0:
        dis=prof.objects.get(usr__id=request.user.id)
        display["data"]=dis
        if request.method=="POST":
            fname=request.POST["fname"]
            lname=request.POST["lname"]
            email=request.POST['email']
            ph_pro=request.POST['phn']
            state=request.POST['state']
            city=request.POST['city']
            street=request.POST['street']

            up_user=User.objects.get(id=request.user.id)
            up_user.first_name=fname
            up_user.last_name=lname
            up_user.email=email
            up_user.save()
            dis.ph_pro=ph_pro
            dis.state=state
            dis.city=city
            dis.street=street
            dis.save()
            if "imgs" in request.FILES:
                img=request.FILES["imgs"]
                dis.img_pro=img
                dis.save()
                messages.info(request,"Image uploaded successfully")
                return redirect("pro")
            messages.info(request,"profile uploaded successfully")
            return redirect("pro")
    return render(request,"updateprofile.html",display)