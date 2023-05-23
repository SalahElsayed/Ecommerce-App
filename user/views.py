# views.py
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.views import PasswordResetView  # Password Reset View 
from .serializers import UserSerializer, PasswordResetSerializer

# User Registration View 
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer


# User Login View 
class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    
# Password Reset View 
class PasswordResetAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Password reset email has been sent."}, status=status.HTTP_200_OK)

    def get_serializer(self, *args, **kwargs):
        return PasswordResetSerializer(*args, **kwargs)