from django.shortcuts import render
from rest_framework import status 
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserLoginSerializer, UserProfileSerializer, UserRegistrationSerializer
from .models import User

# Create your views here.

# Template views
def register_page(request):
    return render(request, 'accounts/register.html')

def login_page(request):
    return render(request, 'accounts/login.html')

def dashboard_page(request):
    return render(request, 'accounts/dashboard.html')

class RegisterView(APIView):
    permission_classes= [AllowAny]

    def post (self, request):
        serializer= UserRegistrationSerializer(data= request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'id': user.id,
                'username':user.username,
                'email': user.email,
                'token': user.token
            }, status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView (APIView):
    permission_classes= [AllowAny]

    def post(self, request):
        serializer=UserLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProfileView(RetrieveUpdateAPIView):
    serializer_class= UserProfileSerializer
    authentication_classes= [TokenAuthentication]

    def get_object(self):
        return self.request.user
