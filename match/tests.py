from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from match.models import human, Subject ,Wantmatch,Review,Matched


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.post('/')
        self.assertRedirects(response,'/accounts/login/')
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.client.login(username= 'testuser', password= '12345')
        response2 = self.client.post('/')
        self.assertTemplateUsed(response2, 'home.html')

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


class RequestTest(TestCase):

    def test_sent_request(self):
        stefanie_user = User.objects.create_user('stefanie01', 'stfanie@email.com', 'stefaniepassword')
        eric_user = User.objects.create_user('eric01', 'eric@email.com', 'ericpassword')
        johnny = human.objects.create(name='johnny01')
        johnny_user = User.objects.create(username='johnny01')
        johnny_user.set_password('johnnypassword')
        johnny_user.save()
        self.client.login(username='testuser', password='12345')
        Subject.objects.create(name='Math2')
        stefanie_subject = Subject.objects.get(name='Math2')
        stefanie = human.objects.create(name='stefanie01')
        stefanie.subject.add(stefanie_subject)

        Subject.objects.create(name='Physic')
        eric_subject = Subject.objects.get(name='Physic')
        eric = human.objects.create(name='eric01')
        eric.subject.add(eric_subject)
        self.client.login(username="johnny01",password="johnnypassword")
        self.client.post(f'/{ eric.name } /matching/')
        self.client.post(f'/matching/{ stefanie.name }/')
        print(reverse('matching', args=['johnny01']))

        wmcount = Wantmatch.objects.all()
        self.assertEqual(wmcount.count(),2)

        firstwm = wmcount[0]
        secondwm = wmcount[1]

        self.assertEqual(firstwm.name, 'johnny01')
        self.assertEqual(secondwm.name, 'johnny01')
'''
    def test_cancel_request(self):
        User.objects.create_user('johnny01', 'johnny@email.com', 'johnnypassword')
        User.objects.create_user('stefanie01', 'stfanie@email.com', 'stefaniepassword')
        User.objects.create_user('eric01', 'eric@email.com', 'ericpassword')
        human.objects.create(name='johnny01')

        Subject.objects.create(subject_name='Math2')
        stefanie_subject = Subject.objects.get(subject_name='Math2')
        stefanie = human.objects.create(name='stefanie01')
        stefanie.good_subject.add(stefanie_subject)

        Subject.objects.create(subject_name='Physic')
        eric_subject = Subject.objects.get(subject_name='Physic')
        eric = human.objects.create(name='eric01')
        eric.good_subject.add(eric_subject)

        self.client.login(username="johnny01", password="johnnypassword")

        # johnny sends request to stefanie and eric.
        request_johnny_to_eric = Wantmatch.objects.create(request_list='johnny01')
        johnny_sent_to_eric = human.objects.get(name='eric01')
        johnny_sent_to_eric.wantmatch.add(request_johnny_to_eric)

        request_johnny_to_stefanie = Wantmatch.objects.create(request_list='johnny01')
        johnny_sent_to_stefanie = human.objects.get(name='stefanie01')
        johnny_sent_to_stefanie.wantmatch.add(request_johnny_to_stefanie)

        count_request = Wantmatch.objects.all()
        self.assertEqual(count_request.count(), 2)

        self.client.post(f'/{ eric.id }/Unmatched/')

        count_request = Wantmatch.objects.all()
        self.assertEqual(count_request.count(), 1)

        first_request = count_request[0]
        self.assertEqual(first_request.name, 'johnny01')

    def test_accept_request(self):
        User.objects.create_user('johnny01', 'johnny@email.com', 'johnnypassword')
        User.objects.create_user('stefanie01', 'stfanie@email.com', 'stefaniepassword')
        User.objects.create_user('eric01', 'eric@email.com', 'ericpassword')
        Userinfo.objects.create(name='johnny01', fullname='Jonhny', lastname='Walker', age='21', school='kmutnb')

        Subject.objects.create(subject_name='Math2')
        stefanie_subject = Subject.objects.get(subject_name='Math2')
        stefanie = Userinfo.objects.create(name='stefanie01', fullname='Stefanie', lastname='Snow', age='21', school='kmutnb')
        stefanie.good_subject.add(stefanie_subject)

        Subject.objects.create(subject_name='Physic')
        eric_subject = Subject.objects.get(subject_name='Physic')
        eric = Userinfo.objects.create(name='eric01', fullname='Eric', lastname='Runner', age='21', school='kmutnb')
        eric.good_subject.add(eric_subject)

        # login as Stefanie
        self.client.login(username="stefanie01", password="stefaniepassword")

        # johnny and eric send request to stefanie.
        request_johnny_to_stefanie = request_class.objects.create(request_list='johnny01')
        johnny_sent_to_stefanie = Userinfo.objects.get(name='stefanie01')
        johnny_sent_to_stefanie.request.add(request_johnny_to_stefanie)

        request_eric_to_stefanie = request_class.objects.create(request_list='eric01')
        eric_sent_to_stefanie = Userinfo.objects.get(name='stefanie01')
        eric_sent_to_stefanie.request.add(request_eric_to_stefanie)
'''