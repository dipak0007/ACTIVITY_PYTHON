from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views  

from .views import *


urlpatterns = [
    # Authentication urls
    path('ragistration/',ragistration_page_view,name='ragistration_page_view'),
    path('otp_verify/',genrate_otp_page,name='genrate_otp_page'),
    path('login/',login_page_view,name='login_page_view'),
    path('forgotpass/',forgot_pass_page,name='forgot_pass_page'),    

    path('logout/',logout,name='logout'),    

 
    path('base/',base_page_view,name='base_page_view'),
    path('',index_page_view,name='index_page_view'),
    path('profile/',profile_page_view,name='profile_page_view'),
    path('contact/',contactus_page_view,name='contactus_page_view'),
    path('about/',about_page_view,name='about_page_view'),
    path('shopping/',my_shopping_page,name='my_shopping_page'),
    path('cart/',cart_page_view,name='cart_page_view'),
    path('cart/pay/<amt>',pay,name="pay"),
    path('cart/<str:product_id>/', add_item_in_cart, name='add_item_in_cart'),
    path('cart/pay/<str:amt>/',pay, name='pay'),

    path('cart/order_confirm',order_confirm,name='order_confirm'),
    path('my_orders/',my_orders,name='my_orders'),


    



    path('profile-update/', update_personal_info, name='update_personal_info'),
    path('add_address_view/', add_address_view, name='add_address_view'),


]