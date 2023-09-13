from .models import SUBCategories
from rest_framework import serializers


class SUBCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SUBCategories
        fields = "__all__"
        #extra_kwargs = {'category_name': {'required': False}}

class subCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SUBCategories
        fields = ['isactive']
