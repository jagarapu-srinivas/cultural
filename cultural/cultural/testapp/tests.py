from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.

class SimplePageTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass1234')

    def test_pages_require_login(self):
        for name in ['agriculture', 'food']:
            response = self.client.get(reverse(name))
            self.assertRedirects(response, f"/login/?next=/" + name + '/')

    def test_pages_with_auth(self):
        self.client.login(username='tester', password='pass1234')
        for name in ['agriculture', 'food']:
            response = self.client.get(reverse(name))
            self.assertEqual(response.status_code, 200)
            # each page should contain at least one key phrase
            if name == 'agriculture':
                self.assertContains(response, 'Seasonal Farming')
            else:
                self.assertContains(response, 'Festive Dishes')

    def test_festival_content(self):
        self.client.login(username='tester', password='pass1234')
        response = self.client.get(reverse('festival'))
        self.assertContains(response, 'Baisakhi')

    def test_home_includes_links(self):
        # authenticated user should see new section links on home
        self.client.login(username='tester', password='pass1234')
        response = self.client.get(reverse('home'))
        self.assertContains(response, reverse('agriculture'))
        self.assertContains(response, reverse('food'))

