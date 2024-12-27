from rest_framework import serializers
from .models import MyEmployees

class MyEmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyEmployees
        fields='__all__'

