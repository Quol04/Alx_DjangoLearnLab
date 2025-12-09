from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError


from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, style ={'input_type':'password'})
    token = serializers.CharField(read_only = True)

    class Meta :
        model = User
        fields = ['id','username','email','password','bio','profile_picture','token']

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return value 
    
    def create(self , validated_data):
        password = validated_data.pop('password')
        user = User (**validated_data)

        user.set_password(password)
        user.save()

        token, _ = Token.objects.get_or_create(user= user)
        # Attach token to serializer output
        user.token = token.key

        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password= serializers.CharField(write_only= True, style = {'input-style':'password'})
    token = serializers.CharField(read_only= True)

    def validate(self, attrs):
        password = attrs.get('password')
        username = attrs.get('username')
        user = authenticate(username= username, password= password)

        if not user:
            raise serializers.ValidationError('Invalid Credentials')
        
        token, _ = Token.objects.get_or_create(user= user)

        return {'token': token.key}

class UserProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(read_only= True)
    following_count = serializers.IntegerField(read_only= True)

    class Meta :
        model = User
        fields= ['id','email','username','bio','profile_picture','followers_count','following_count']
        read_only_fields =['email','username','followers_count','following_count']
