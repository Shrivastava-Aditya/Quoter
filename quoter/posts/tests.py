from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Posts

class PostsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email='test@gmail.com',
            password='adminadmin',
        )
        self.post = Posts.objects.create(
            body='A new Quote!',
            user = self.user,
        )

    def test_post_string(self):
        post = Posts(body='A sample Quote!')
        self.assertEqual(str(post),post.body)

    def test_post_content(self):
        self.assertEqual(f'{self.post.user}','testuser')
        self.assertEqual(f'{self.post.body}','A new Quote!')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'A new Quote!')
        self.assertTemplateUsed(response,'home.html')

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'),{
        'body' : 'A new Quote',
        'user' : self.user,
        })
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'A new Quote')


# Create your tests here.
