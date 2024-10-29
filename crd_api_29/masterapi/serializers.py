from rest_framework import serializers

from .models import MyBookModel

class MyBookSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = MyBookModel
        fields = '__all__'