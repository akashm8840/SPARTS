from pickle import FALSE
from django.shortcuts import render,get_object_or_404,reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.contrib import messages
from django.http import HttpRequest, HttpResponse,JsonResponse
from . models import *
from Register.models import*
# Create your views here.
def index(request):
    cat=category.objects.all()
    dic={}
    dic["cate"]=cat
    return render(request,"index.html",dic)

def it_about(request):
    return render(request,"it_about.html")
def it_blog_detail(request):
    return render(request,"it_blog_detail.html")
def it_blog_grid(request):
    return render(request,"it_blog_grid.html")
def it_blog(request):
        return render(request,"it_blog.html")
def it_career(request):
    return render(request,"it_career.html")
# def it_cart(request):
#     return render(request,"it_cart.html")
def it_checkout(request):
    return render(request,"it_checkout.html")
def it_contact_2(request):
    return render(request,"it_contact_2.html")
def it_contact (request):
    if request.method=="POST":
        sub=request.POST["sub"]
        msg=request.POST["msg"]
        num=request.POST["num"]
        usr=get_object_or_404(User,id=request.user.id)
        cn=contact(user=usr,contnum=num,message=msg,subject=sub)
        cn.save()
    return render(request,"it_contact.html")
def it_data_recovery(request):
    return render(request,"it_data_recovery.html")
def it_error(request):
    return render(request,"it_error.html")
def it_faq(request):
    return render(request,"it_faq.html")
def it_home_dark(request):
    return render(request,"it_home_dark.html")
def it_home(request):
    return render(request,"it_home.html")
def it_mobile_service(request):
     return render(request,"it_mobile_service.html")
def it_network_solution(request):
    return render(request,"it_network_solution.html")
def it_news(request):
    return render(request,"it_news.html")
def it_price(request):
    return render(request,"it_price.html")
def it_privacy_policy(request):
    return render(request,"it_privacy_policy.html")
def it_service_detail(request):
        return render(request,"it_service_detail.html")
def it_service_list(request):
    return render(request,"it_service_list.html")
def it_service(request):
     return render(request,"it_service.html")
def it_shop_detail(request):
    return render(request,"it_shop_detail.html")
def it_sh(request,cid):
    dic={}
    sp=category.objects.get(id=cid)
    pro=SpareParts.objects.filter(cat=sp)
    dic["prod"]=pro
    
    return render(request,"it_shop.html",dic)
def it_shop(request):
    dic={}
    pro=SpareParts.objects.all()
    dic["prod"]=pro
    
    return render(request,"it_shop.html",dic)
def it_techn_support(request):
    return render(request,"it_techn_support.html")
def it_term_condition(request):
    return render(request,"it_term_condition.html")
def make_appointment(request):
    return render(request,"make_appointment.html")
def registration(request):
    return render(request,"registration.html")

def login(request):
    return render(request,"login.html")
def login(request):
    return render(request,"login.html")
def Profile(request):
    return render(request,"profile.html")
def uppro(request):
    return render(request,"updateprofile.html")
def Cart(request):
    dic={}
    item=cart.objects.filter(usr_id=request.user.id,status=False)
    dic['item']=item
    if request.user.is_authenticated:
        if request.method=='POST':
            cried=request.POST['sid']
            quan=request.POST['qty']
            is_exist=cart.objects.filter(cour_id=cried,usr_id=request.user.id,status=False)
            if len(is_exist)>0:
             dic["msg"]="item already in cart"
            else:
                cor=get_object_or_404(SpareParts,id=cried)
                usr=get_object_or_404(User,id=request.user.id)
                crt=cart(cour=cor,usr=usr,quantity=quan)
                crt.save()
                dic["msg"]="{}Added in ur Cart"
        else:
            dic["status"]="please login first"        
    return render(request,"it_cart.html",dic)
def r_cart(request):
    if "delete_cart" in request.GET:
        id = request.GET["delete_cart"]
        cartobj = get_object_or_404(cart, id=id)
        cartobj.delete()
    return HttpResponse(1)
def get_cart_data(request):
    items = cart.objects.filter(usr__id=request.user.id, status=False)
    sale,quantity =0,0
    for i in items:
        sale += float(i.cour.price)*i.quantity
        
        quantity+= float(i.quantity)

    res = {
        "offer":sale,"quan":quantity,
    }
    return JsonResponse(res)
    
def change_quan(request):
    if "quantity" in request.GET:
        cid = request.GET["cid"]
        qty = request.GET["quantity"]
        cart_obj = get_object_or_404(cart,id=cid)
        cart_obj.quantity = qty
        cart_obj.save()
        return HttpResponse(cart_obj.quantity)
    elif "delete_cart" in request.GET:    
        id = request.GET["delete_cart"]
        cart_obj = get_object_or_404(cart,id=id)
        cart_obj.delete()
        return HttpResponse(1)



def process_payment(request):
    items = cart.objects.filter(usr_id__id=request.user.id,status=False)
    products=""
    amt=0
    inv = "INV10001-"
    cart_ids = ""
    p_ids =""
    for j in items:
        products += str(j.cour.product)+"\n"
        p_ids += str(j.cour.id)+","
        amt += float(j.cour.price)
        inv +=  str(j.id)
        cart_ids += str(j.id)+","

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': str(amt/77),
        'item_name': products,
        'invoice': inv,
        'notify_url': 'http://{}{}'.format("127.0.0.1:8000",
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format("127.0.0.1:8000",
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format("127.0.0.1:8000",
                                              reverse('payment_cancelled')),
    }
    usr = User.objects.get(username=request.user.username)
    ord = Order(cust_id=usr,cart_ids=cart_ids,product_ids=p_ids)
    ord.save()
    ord.invoice_id = str(ord.id)+inv
    ord.save()
    request.session["order_id"] = ord.id
    
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'process_payment.html', {'form': form})

def payment_done(request):
    if "order_id" in request.session:
        order_id = request.session["order_id"]
        ord_obj = get_object_or_404(Order,id=order_id)
        ord_obj.status=True
        ord_obj.save()
        
        for i in ord_obj.cart_ids.split(",")[:-1]:
            cart_object = cart.objects.get(id=i)
            cart_object.status=True
            cart_object.save()
    return render(request,"payment_success.html")

def payment_cancelled(request):
    return render(request,"payment_failed.html")
def sgpro(request,bid):
    dic={}
    prs=SpareParts.objects.get(id=bid)
    dic["prs"]=prs
    return render(request,"it_shop_detail.html",dic)
def search(request):
    product_dic={}
    if request.method=="POST":
        sr=request.POST["ser"]
        pr=SpareParts.objects.filter(product__icontains=sr)
        product_dic["prod"]=pr
    return render(request,"it_shop.html",product_dic)

def feed(request):
    user=contact.objects.filter(user_id=request.user.id)
    if request.method=="POST":
        title=request.POST['title']
        revbody=request.POST['revbody']
        pro_id=request.POST['bid']
        print(title, revbody)
        user=get_object_or_404(User,id=request.user.id)
        pro=get_object_or_404(SpareParts,id=pro_id)
        co=feedback( user=user,title=title,revbody=revbody,ratpro=pro)
        co.save()
        messages.info(request, "Feedback send successfully...")
    return render(request,'it_shop_detail.html')

def Whishlist(request):
    dic={}
    item=whishlist.objects.filter(user_id=request.user.id,status=False)
    dic['item']=item
    if request.user.is_authenticated:
        if request.method=='POST':
            crd=request.POST['vid']
            qua=request.POST['qtn']
            is_exist=whishlist.objects.filter(product_id=crd,user_id=request.user.id,status=False)
            if len(is_exist)>0:
             dic["msg"]="item already in whishlist"
            else:
                cor=get_object_or_404(SpareParts,id=crd)
                usr=get_object_or_404(User,id=request.user.id)
                wsh=whishlist(product=cor,user=usr,quantity=qua)
                wsh.save()
                dic["msg"]="{}Added in ur Whishlist"
        else:
            dic["status"]="please login first"        
    return render(request,"whishlist.html",dic)   

def remove_package(request):
    if "delete_cart" in request.GET:
        id=request.GET["delete_cart"]
        cartobj=get_object_or_404(whishlist,id=id)
        cartobj.delete()
    return HttpResponse(1)
# def get_whishlist_data(request):
#     items = whishlist.objects.filter(user__id=request.user.id, status=False)
#     sale,quantity =0,0
#     for i in items:
#         sale += float(i.cour.price)*i.quantity
        
#         quantity+= float(i.quantity)

#     res = {
#         "offer":sale,"quan":quantity,
#     }
#     return JsonResponse(res)
    
# def change_qun(request):
#     if "quantity" in request.GET:
#         cid = request.GET["cid"]
#         qty = request.GET["quantity"]
#         whishlist_obj = get_object_or_404(whishlist,id=cid)
#         whishlist_obj.quantity = qty
#         whishlist_obj.save()
#         return HttpResponse(whishlist_obj.quantity)
#     elif "delete_whishlist" in request.GET:    
#         id = request.GET["delete_whishlist"]
#         whishlist_obj = get_object_or_404(whishlist,id=id)
#         whishlist_obj.delete()
#         return HttpResponse(1)    