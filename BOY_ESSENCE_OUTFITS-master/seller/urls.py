from django.urls import path
from .views import *

urlpatterns = [
    path('', seller_index_view, name='seller_index_view'),
]