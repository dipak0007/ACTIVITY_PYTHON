from django.shortcuts import render

from .serializers import MyBookSerializerModel
from .models import MyBookModel

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def mydata(request):
    if request.method == 'POST':
        serializer = MyBookSerializerModel(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'GET':
        get_mydata = MyBookModel.objects.all()
        serializer = MyBookSerializerModel(get_mydata,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

@api_view(['GET','PUT','PATCH','DELETE'])
def my_manage_details(request,book_id):
    try:
        get_info = MyBookModel.objects.get(id=book_id)
    except MyBookModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MyBookSerializerModel(get_info)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    if request.method == 'PUT':
        serializer = MyBookSerializerModel(get_info,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    if request.method == 'PATCH':
        serializer = MyBookSerializerModel(get_info,data=request.data,partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        del_id = get_info
        del_id.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)

