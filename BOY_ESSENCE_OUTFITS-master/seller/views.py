from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def seller_index_view(request):
    return HttpResponse("I am seller")
