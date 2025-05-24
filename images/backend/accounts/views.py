from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CustomerUser
from .utils import generate_otp, verify_otp
from .serializers import MyTokenObtainPairSerializer, UserRegistrationSerializer


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generate OTPs
            email_otp = generate_otp()
            mobile_otp = generate_otp()
            user.email_otp = email_otp
            user.mobile_otp = mobile_otp
            user.save()

            # Send email OTP
            send_mail(
                'Email Verification OTP',
                f'Your OTP for email verification is: {email_otp}',
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )

            # Simulate sending SMS OTP
            print(f"Mobile OTP for {user.mobile_number}: {mobile_otp}")

            return Response({
                "message": "User registered successfully. Verify OTPs to activate account.",
                "user_id": user.id
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user_id = request.data.get('user_id')
        email_otp = request.data.get('email_otp')
        mobile_otp = request.data.get('mobile_otp')

        user = get_object_or_404(CustomerUser, id=user_id)

        if verify_otp(email_otp, user.email_otp) and verify_otp(mobile_otp, user.mobile_otp):
            user.is_email_verified = True
            user.is_mobile_verified = True
            user.email_otp = None
            user.mobile_otp = None
            user.save()
            return Response({"message": "OTP verification successful. You can now log in."})
        else:
            return Response({"error": "Invalid OTPs."}, status=status.HTTP_400_BAD_REQUEST)


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class ResendOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user_id = request.data.get('user_id')
        user = get_object_or_404(CustomerUser, id=user_id)

        if user.is_email_verified and user.is_mobile_verified:
            return Response({"message": "User is already verified."}, status=status.HTTP_400_BAD_REQUEST)

        # Regenerate OTPs
        email_otp = generate_otp()
        mobile_otp = generate_otp()
        user.email_otp = email_otp
        user.mobile_otp = mobile_otp
        user.save()

        # Send email OTP
        send_mail(
            'Email Verification OTP (Resent)',
            f'Your new email OTP is: {email_otp}',
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )

        # Simulate mobile OTP sending
        print(f"Resent Mobile OTP for {user.mobile_number}: {mobile_otp}")

        return Response({"message": "OTP resent successfully."}, status=status.HTTP_200_OK)
