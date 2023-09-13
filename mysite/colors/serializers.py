from .models import Colors
from rest_framework import serializers

class ColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = "__all__"

class COLORSSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = ['isactive']