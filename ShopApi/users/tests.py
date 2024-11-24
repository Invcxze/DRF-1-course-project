from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient

from .models import User
from .test_base import login_data, signup_data_error, test_user_data


# Create your tests here.
class TestViews(APITestCase):
    def setUp(self) -> None:
        self.base_url = "http://127.0.0.1:8000/api/v1"
        self.user_client = RequestsClient()
        User.objects.create(fio="mama", email="mama@mama.ru", password="password_13131232131")

    def test_signup_success(self):
        url = self.base_url + "/signup"

        response = self.user_client.post(url, data=login_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_signup_error_400(self):
        url = self.base_url + "/signup"

        response = self.user_client.post(url, data=signup_data_error)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_success(self):
        url = self.base_url + "/login"

        response = self.user_client.post(url, data=test_user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.text)
