from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post, Subscription

User = get_user_model()


class YourAppTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')

    def test_create_post_view(self):
        self.client.login(username=self.user.username, password='password')
        response = self.client.post(reverse('create_post'), {'title': 'Test Title', 'content': 'Test Content'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(Post.objects.filter(title='Test Title', content='Test Content').exists())

    def test_view_post_view(self):
        post = Post.objects.create(title='Test title', content='Test content')
        response = self.client.get(reverse('view_post', args=[post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)
        self.assertContains(response, post.content)

    def test_registration_view(self):
        response = self.client.post(reverse('register'),
                                    {'username': 'testuser', 'email': 'test@example.com', 'password1': 'password',
                                     'password2': 'password'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': self.user.username, 'password': 'password'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertIn('_auth_user_id', self.client.session)

    def test_process_payment(self):
        response = self.client.post(reverse('process_payment'),
                                    {'credit_card_number': '4242424242424242', 'expiration_date': '12/22',
                                     'cvv': '123'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Payment Success")



