from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from .models import CustomerUser



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['is_email_verified'] = user.is_email_verified
        token['is_mobile_verified'] = user.is_mobile_verified
        return token


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = CustomerUser
        fields = ['username', 'email', 'mobile_number', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        if CustomerUser.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email": "This email already exists."})
        if CustomerUser.objects.filter(mobile_number=attrs['mobile_number']).exists():
            raise serializers.ValidationError({"mobile_number": "This mobile number already exists."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = CustomerUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            mobile_number=validated_data['mobile_number'],
            password=validated_data['password']
        )
        return user
