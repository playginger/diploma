from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post


class YourAppTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', email='test@example.com',
                                                         password='password', phone_number='1234567890')

    def test_create_post_view(self):
        self.client.login(username=self.user.username, password='password')
        response = self.client.post(reverse('users:create_post'), {'title': 'Test Title', 'content': 'Test Content'})
        self.assertEqual(response.status_code, 302)
        # self.assertRedirects(response, reverse('users:home'))
        self.assertTrue(Post.objects.filter(title='Test Title', content='Test Content').exists())

    def test_view_post_view(self):
        post = Post.objects.create(author=self.user, title='Test Title', content='Test Content')
        response = self.client.get(reverse('users:view_post', args=[post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)
        self.assertContains(response, post.content)

    def test_registration_view(self):
        response = self.client.post(reverse('users:register'),
                                    {'username': 'testuser2', 'email': 'test2@example.com', 'password1': 'password',
                                     'password2': 'password', 'phone_number': '9876543210'})
        self.assertEqual(response.status_code, 200)



