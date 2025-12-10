from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


from .models import User
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.save()

        token, _ = Token.objects.get_or_create(user=user)
        data = UserSerializer(user, context={'request': request}).data

        return Response({
            'user': data,
            'token': token.key,
        }, status=status.HTTP_201_CREATED)


#

class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]


    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)

        data = UserSerializer(user, context={'request': request}).data

        return Response({
            'user': data,
            'token': token.key,
        }, status=status.HTTP_200_OK)



class ProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


    def get_object(self):
        return self.request.user



#  view other users by username
class UserDetailAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = 'username'
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]