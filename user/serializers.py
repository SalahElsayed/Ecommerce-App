from rest_framework import serializers 
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from user.models import CustomUser 

# User Serializer 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
# Password Reset Serializer 
# serializers.py

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    def validate_email(self, value):
        form = PasswordResetForm(data=self.initial_data)
        if not form.is_valid():
            raise serializers.ValidationError("Invalid email.")
        return value

    def save(self):
        form = PasswordResetForm(data=self.initial_data)
        form.is_valid()
        form.save(use_https=self.context['request'].is_secure(), token_generator=default_token_generator)
