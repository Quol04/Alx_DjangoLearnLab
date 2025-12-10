from django.urls import path
from .views import RegisterAPIView, LoginAPIView, ProfileAPIView, UserDetailAPIView


app_name = 'accounts'


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
    path('users/<str:username>/', UserDetailAPIView.as_view(), name='user-detail'),
]