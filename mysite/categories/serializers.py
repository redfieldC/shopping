from .models import Categories
from rest_framework import serializers

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"
        extra_kwargs = {'category_name': {'required': False}}


class CATEGORIESSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['isactive']
        