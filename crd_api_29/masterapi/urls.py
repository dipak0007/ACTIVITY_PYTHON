from django.contrib import admin
from django.urls import path

from .views import mydata
from .views import my_manage_details

urlpatterns = [
    path('API/',mydata,name='mydata'),
    path('API/<int:book_id>',my_manage_details,name='my_manage_details'),
]
