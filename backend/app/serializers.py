from rest_framework import serializers
from .models import Customer

# serializer Customer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "id", 
            'document',  
            'first_name', 
            'last_name', 
            'email',             
            'phone'
        )
