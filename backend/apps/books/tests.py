from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginTestCase(TestCase):
    def setUp(self):
        #テストユーザーをセットアップ
        self.user = User.objects.create_user(
            email= 'test@exsample.com',
            password= 'password123'
        )

    def test_login_success(self):
        #ログインが成功したパターン
        response = self.client.post(reverse('token'), {
            'email': 'test@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)

    def test_login_failure(self):
        #ログインが失敗したパターン
        response = self.client.post(reverse('token'), {
            'email': 'test@example.com',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 400)
        self.assertNotIn('token', response.data)