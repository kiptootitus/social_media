from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import  ResendOTPView, UserRegistrationView, MyObtainTokenPairView, VerifyOTPView
urlpatterns = [
  path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
  path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('register/', UserRegistrationView.as_view(), name='user_registration'),
  path('verify_otp/<int:user_id>/', VerifyOTPView.as_view(), name='verify_otp'),
  path('resend-otp/', ResendOTPView.as_view(), name='resend_otp'),

]