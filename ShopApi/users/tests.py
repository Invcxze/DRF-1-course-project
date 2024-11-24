from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, RequestsClient

from .models import User
from .test_base import login_data, signup_data_error, signup_data


# Create your tests here.
class TestViews(APITestCase):
    def setUp(self) -> None:
        self.base_url = "http://127.0.0.1:8000/api/v1"
        self.user_client = RequestsClient()
        self.user = User.objects.create(email="mama@mama.ru", fio="mama", is_active=True)
        self.user.set_password("password_13131232131")
        self.user.save()

    def test_signup_success(self):
        url = self.base_url + "/signup"
        response = self.user_client.post(url, data=signup_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_signup_error_400(self):
        url = self.base_url + "/signup"
        response = self.user_client.post(url, data=signup_data_error)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_logout_error_403(self):
        url = self.base_url + "/logout"
        response = self.user_client.post(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_login_success(self):
        url = self.base_url + "/login"
        response = self.user_client.post(url, data=login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout_success(self):
        token = Token.objects.create(user=self.user)
        self.user_client.headers.update({'Authorization': f'Bearer {token.key}'})

        url = self.base_url + "/logout"
        response = self.user_client.post(url)  # Используем POST вместо GET
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.text)
        self.assertFalse(Token.objects.filter(user=self.user).exists())
