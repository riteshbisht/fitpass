from rest_framework import serializers
from users.models import User

class UserActiveInactiveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('is_active',)
