# urls.py
from django.urls import path
from .views import UserRegistrationView, UserLoginView, PasswordResetAPIView

# Urlpatterns 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_register'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('password/reset/', PasswordResetAPIView.as_view(), name='password_reset'),

]
