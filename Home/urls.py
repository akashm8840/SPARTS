from django.urls import path
from.import views

urlpatterns = [
    path("",views.index,name="ind"),
    path("about",views.it_about,name="about"),
    path("blog_detail",views.it_blog_detail,name="blog_detail"),
    path("blog_grid",views.it_blog_grid,name="blog_grid"),
    path("blog",views.it_blog,name="blog"),
    path("career",views.it_career,name="career"),
    path("checkout",views.it_checkout,name="checkout"),
    path("contact_2",views.it_contact_2,name="contact_2"),
    path("contact",views.it_contact,name="contact"),
    path("rec",views.it_data_recovery,name="recovery"),
    path("error",views.it_error,name="error"),
    path("faq",views.it_faq,name="faq"),
    path("homed",views.it_home_dark,name="home_dark"),
    path("home",views.it_home,name="home"),
    path("mservice",views.it_mobile_service,name="mobile_service"),
    path("ns",views.it_network_solution,name="network_solution"),
    path("news",views.it_news,name="news"),
    path("price",views.it_price,name="price"),
    path("policy",views.it_privacy_policy,name="privacy_policy"),
    path("sdetail",views.it_service_detail,name="service_detail"),
    path("slist",views.it_service_list,name="service_list"),
    path("service",views.it_service,name="service"),
    path("shopdetail",views.it_shop_detail,name="shop_detail"),
    path("shop",views.it_shop,name="shop"),
    path("<int:cid>",views.it_sh,name="shop"),
    path("support",views.it_techn_support,name="tech_support"),
    path("term",views.it_term_condition,name="term_condition"),
    path("appointment",views.make_appointment,name="make_appointment"),
    path("registration",views.registration,name="registration"),
    path("login",views.login,name="login"),
    path("profile",views.Profile,name="profile"),
     path("uppro",views.uppro,name="uppro"),
    path("cart",views.Cart,name="crt"),
    path("r_cart",views.r_cart,name="r_cart"),
    #path("up",views.upreg,name="updateregistration"),
     path("get_cart_data",views.get_cart_data,name="get_cart_data"), 
    path("change_quan",views.change_quan,name="change_quan"),
    path("remove_package",views.remove_package,name="remove_package"),
    path("process_payment",views.process_payment,name="process_payment"),
    path("payment_done",views.payment_done,name="payment_done"),
    path("payment_cancelled",views.payment_cancelled,name="payment_cancelled"),
    path("sgn/<int:bid>",views.sgpro,name="sgn1"),
    path("ser",views.search,name="ser"),
    path("feedback",views.feed,name="Feedback"),
    path("whishlist",views.Whishlist,name="wsh"),
    
]

