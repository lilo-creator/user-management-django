from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class UserTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_user_created(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.username, 'testuser')

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_profile_requires_login(self):
        response = self.client.get(reverse('profile'))
        self.assertRedirects(response, '/accounts/login/?next=/users/profile/')

    def test_profile_logged_in(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')
