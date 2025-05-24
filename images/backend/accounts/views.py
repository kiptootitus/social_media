from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import MyTokenObtainPairSerializer, UserRegistrationSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView


class UserRegistrationView(APIView):
  def post(self, request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({
        "message": "User registered sucessfull"
      }, status=status.HTTP_201_CREATED)  
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
class MyObtainTokenPairView(TokenObtainPairView):
  permission_classes = (AllowAny,)
  serializer_class = MyTokenObtainPairSerializer

