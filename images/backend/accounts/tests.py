from rest_framework.test import APITestCase
from django.urls import reverse
from .models import CustomerUser

class UserAuthTests(APITestCase):

    def test_register_user(self):
        url = reverse('register')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'mobile_number': '1234567890',
            'password': 'StrongPassword123!',
            'password2': 'StrongPassword123!'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("user_id", response.data)

    def test_verify_otp(self):
        user = CustomerUser.objects.create_user(
            username='verifyuser',
            email='verify@example.com',
            mobile_number='1234567890',
            password='StrongPassword123!',
            email_otp='123456',
            mobile_otp='654321'
        )
        url = reverse('verify_otp')
        data = {
            'user_id': user.id,
            'email_otp': '123456',
            'mobile_otp': '654321'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], 'OTP verification successful. You can now log in.')

    def test_resend_otp(self):
        user = CustomerUser.objects.create_user(
            username='resenduser',
            email='resend@example.com',
            mobile_number='1234567890',
            password='StrongPassword123!',
        )
        url = reverse('resend_otp')
        data = {'user_id': user.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], 'OTP resent successfully.')
