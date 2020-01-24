from django.test import TestCase
from django.contrib.auth.models import User

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_saving_registered(self):
        u = User.objects.get(username='mokinwza')
        u.set_password('Mokza007')
        u.save()
        
        count = User.objects.count()
        self.assertEqual(count, 1)