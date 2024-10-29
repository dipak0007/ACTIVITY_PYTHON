
from django.contrib import admin
from django.urls import path

from .views import myformpage
from .views import show_mydata
from .views import edit_page
from .views import update_mydata
from .views import delete_view

urlpatterns = [
    path('',myformpage,name='myformpage'),
    path('table/',show_mydata,name='show_mydata'),
    path('edit/<int:pk>',edit_page,name='edit_page'),
    path('update/<int:pk>',update_mydata,name='update_mydata'),
    path('delete/<int:pk>',delete_view,name='delete_view'),
]
