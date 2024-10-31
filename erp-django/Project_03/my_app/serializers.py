from rest_framework import serializers
from .models import CRUD

class CRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = CRUD
        fields = '__all__'