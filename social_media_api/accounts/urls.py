from django.urls import path
from .views import RegisterView, LoginView, ProfileView, register_page, login_page, dashboard_page


urlpatterns=[
    # API endpoints
    path("register/", RegisterView.as_view(), name='register'),
    path("login/", LoginView.as_view(), name='login'),
    path("profile/", ProfileView.as_view(), name='profile'),
    
    # Template pages
    path("register-page/", register_page, name='register_page'),
    path("login-page/", login_page, name='login_page'),
    path("dashboard/", dashboard_page, name='dashboard'),
]