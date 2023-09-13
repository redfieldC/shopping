from .models import Products
from rest_framework import serializers

class POLLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
        