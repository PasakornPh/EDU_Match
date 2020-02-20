from django.test import TestCase
from django.contrib.auth.models import User

from match.models import human, Subject


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

class HumanModelTest(TestCase):
    def test_saving_fav_subject(self):
        first_user = human.objects.create(name='first_user')
        firstsubject = Subject.objects.create(name='first_subject')
        first_user.subject.add(firstsubject)

        second_user = human.objects.create(name='second_user')
        second_subject = Subject.objects.create(name='second_subject')
        second_user.subject.add(second_subject)

        all_user= human.objects.all()
        first_saved_user=all_user[0]
        second_saved_user=all_user[1]
        self.assertEqual(all_user.count(),2)
        self.assertEqual(first_saved_user.subject.first().name, 'first_subject')
        self.assertEqual(second_saved_user.subject.first().name, 'second_subject')

class SignUpTest(TestCase):
    def test_user_signup(self):
        self.user1 =  User.objects.create_user(username='testuser', password='Password12345', email='test@example.com')
        self.user1.save()

        users = User.objects.all()
        self.assertEqual(users.count(), 1)

    def test_two_user_signup(self):
        self.user1 = User.objects.create_user(username='testuser', password='Password12345', email='test@example.com')
        self.user1.save()

        self.user2 = User.objects.create_user(username='testuser2', password='Password12345', email='test2@example.com')
        self.user2.save()

        users = User.objects.all()
        self.assertEqual(users.count(), 2)

class ChangeFirstNameTest(TestCase):
    def test_change_first_name(self):
        self.user1 = User.objects.create_user(username='testuser',
                                              first_name = 'firstname' ,
                                              password='Password12345',
                                              email='test@example.com')
        self.user1.save()

        users = User.objects.get(username='testuser')

        self.assertEqual(users.first_name,'firstname')

        users.first_name = 'change_firstname'
        users.save()

        self.assertEqual(users.first_name, 'change_firstname')




class ChangePasswordTest(TestCase):
    def test_change_password(self):
        self.user1 = User.objects.create_user(username='testuser',
                                              password='Password12345',
                                              email='test@example.com')
        self.user1.save()

        users = User.objects.get(username='testuser')
        hash_password1 = users.password

        users.set_password('Password67890')
        users.save()

        hash_password2 = users.password
        self.assertNotEquals(hash_password1,hash_password2)