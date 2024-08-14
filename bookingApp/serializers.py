
from .models import *
from rest_framework import serializers

# ================ CREATING OF USER ===================
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password',]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user



class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class RoomCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomCategory
        fields = '__all__'
