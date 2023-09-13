from .models import Size
from rest_framework import serializers


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"

class SIZESerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['isactive']

