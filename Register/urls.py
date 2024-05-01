from django.urls import path
from.import views

urlpatterns = [
    path("",views.register,name="reg"),
    path("login",views.login,name="log"),
    path("logout",views.logout,name="logt"),
    path('profile',views.Profile,name='pro'),
    path('uppro/',views.uppro,name='uppro'),
   
]