from rest_framework import serializers


from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField()