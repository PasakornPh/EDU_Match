from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from match.models import human, Subject, Wantmatch, Review, Matched, Chatroomname


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
        kitsanapong = User.objects.create(username='kitsanapong')
        kitsanapong.set_password('kpassword')
        kitsanapong.save()
        pasakorn = User.objects.create(username='pasakorn')
        pasakorn.set_password('mpassword')
        pasakorn.save()
        self.client.login(username='kitsanapong', password='kpassword')
        pasakornh = human.objects.create(name='pasakorn')
        kitsanapongh = human.objects.create(name='kitsanapong')
        self.client.login(username="kitsanapong",password="kpassword")
        chatname = Chatroomname.objects.create(name='kitsanapong' + 'pasakorn')
        chatname.save()
        chatnamer = Chatroomname.objects.get(name='kitsanapong' + 'pasakorn')
        human.objects.get(name='kitsanapong').chatroomname.add(chatnamer)
        human.objects.get(name='pasakorn').chatroomname.add(chatnamer)


        self.client.post(f'/matching/{pasakornh.name}')

        wmcount = Wantmatch.objects.all()
        print('wmcount =',wmcount.count())
        self.assertEqual(wmcount.count(),1)

        firstwm = wmcount[0]

        self.assertEqual(firstwm.name, 'kitsanapong')
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

'''

class HomePageTest(TestCase):

    def test_URL_mapping_to_homepage(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    # delete logo to pass this test.
    def test_rendering_homepageTemplate(self):
        stefanie_user = User.objects.create_user('stefanie01', 'stfanie@email.com', 'stefaniepassword')
        stefanie = Userinfo.objects.create(name='stefanie01', fullname='Stefanie', lastname='Snow', age='20', school='kmutnb')
        self.client.login(username='stefanie01', password='stefaniepassword')
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'tinder/home.html')


    # can not test because search can not usable.
    def test_search_people(self):
        # create users
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
        eric = Userinfo.objects.create(name='eric01', fullname='Eric', lastname='Runner', age='21',school='kmutnb')
        eric.good_subject.add(eric_subject)

        # login as Johnny
        self.client.force_login(User.objects.get_or_create(username='johnny01')[0])
        response = self.client.post('/', data={'subject_find': 'Math2', 'location_school': '', 'filter':''})
        self.assertNotContains(response, 'eric01')
        self.assertContains(response, 'stefanie01')



class ProfileTest(TestCase):

    def test_URL_mapping_to_Profile(self):
        johnny = Userinfo.objects.create(name='johnny01', fullname='Jonhny', lastname='Walker', age='21', school='kmutnb')
        found = resolve('/'+ str(johnny.id) +'/your_subject/')
        self.assertEqual(found.func, your_subject_page)


    def test_rendering_profile(self):
        johnny_user = User.objects.create_user('johnny01', 'johnny@email.com', 'johnnypassword')
        johnny = Userinfo.objects.create(name='johnny01', fullname='Jonhny', lastname='Walker', age='21', school='kmutnb')
        self.client.login(username='johnny01', password='johnnypassword')
        response = self.client.get('/'+ str(johnny.id) +'/your_subject/')
        self.assertTemplateUsed(response, 'tinder/your_subject.html')

    def test_see_profile(self):
        # create user for see profile.
        johnny_user = User.objects.create_user('johnny01', 'johnny@email.com', 'johnnypassword')
        johnny = Userinfo.objects.create(name='johnny01', fullname='Jonhny', lastname='Walker', age='21', school='kmutnb')
        stefanie_user = User.objects.create_user('stefanie01', 'stfanie@email.com', 'stefaniepassword')
        stefanie = Userinfo.objects.create(name='stefanie01', fullname='Stefanie', lastname='Snow', age='21', school='kmutnb')

        # login as Johnny.
        self.client.login(username='johnny01', password='johnnypassword')
        response = self.client.post('/'+ str(johnny.id) +'/your_subject/')
        self.assertContains(response, 'johnny01')
        self.assertContains(response, 'Jonhny')
        self.assertContains(response, 'Walker')
        self.assertContains(response, '21')
        self.assertContains(response, 'kmutnb')
        self.assertNotContains(response, 'stefanie01')


    def test_add_my_subject(self):
        # create users that have their good subject.
        eric = Userinfo.objects.create(name='eric01', fullname='Eric', lastname='Runner', age='21', school='kmutnb')
        Subject.objects.create(subject_name='Physic')
        eric_subject = Subject.objects.get(subject_name='Physic')
        eric.good_subject.add(eric_subject)

        stefanie = Userinfo.objects.create(name='stefanie01', fullname='Stefanie', lastname='Snow', age='21', school='kmutnb')
        Subject.objects.create(subject_name='Math2')
        stefanie_subject = Subject.objects.get(subject_name='Math2')
        stefanie.good_subject.add(stefanie_subject)

        all_subject = Userinfo.objects.all()
        eric_0 = all_subject[0]
        stefanie_1 = all_subject[1]
        self.assertEqual(all_subject.count(),2)
        self.assertEqual(eric_0.good_subject.first().subject_name, 'Physic')
        self.assertEqual(stefanie_1.good_subject.first().subject_name, 'Math2')


class TutorRequestTest(TestCase):

    def test_sent_request(self):
        johnny_user = User.objects.create_user('johnny01', 'johnny@email.com', 'johnnypassword')
        stefanie_user = User.objects.create_user('stefanie01', 'stfanie@email.com', 'stefaniepassword')
        eric_user = User.objects.create_user('eric01', 'eric@email.com', 'ericpassword')
        johnny = Userinfo.objects.create(name='johnny01', fullname='Jonhny', lastname='Walker', age='21', school='kmutnb')

        Subject.objects.create(subject_name='Math2')
        stefanie_subject = Subject.objects.get(subject_name='Math2')
        stefanie = Userinfo.objects.create(name='stefanie01', fullname='Stefanie', lastname='Snow', age='21', school='kmutnb')
        stefanie.good_subject.add(stefanie_subject)

        Subject.objects.create(subject_name='Physic')
        eric_subject = Subject.objects.get(subject_name='Physic')
        eric = Userinfo.objects.create(name='eric01', fullname='Eric', lastname='Runner', age='21', school='kmutnb')
        eric.good_subject.add(eric_subject)
        self.client.login(username="johnny01",password="johnnypassword")

        self.client.post(f'/{ eric.id }/match/')
        self.client.post(f'/{ stefanie.id }/match/')

        count_request = request_class.objects.all()
        self.assertEqual(count_request.count(),2)

        first_request = count_request[0]
        second_request = count_request[1]

        self.assertEqual(first_request.request_list, 'johnny01')
        self.assertEqual(second_request.request_list, 'johnny01')

    def test_cancel_request(self):
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

        self.client.login(username="johnny01", password="johnnypassword")

        # johnny sends request to stefanie and eric.
        request_johnny_to_eric = request_class.objects.create(request_list='johnny01')
        johnny_sent_to_eric = Userinfo.objects.get(name='eric01')
        johnny_sent_to_eric.request.add(request_johnny_to_eric)

        request_johnny_to_stefanie = request_class.objects.create(request_list='johnny01')
        johnny_sent_to_stefanie = Userinfo.objects.get(name='stefanie01')
        johnny_sent_to_stefanie.request.add(request_johnny_to_stefanie)

        count_request = request_class.objects.all()
        self.assertEqual(count_request.count(), 2)

        self.client.post(f'/{ eric.id }/Unmatched/')

        count_request = request_class.objects.all()
        self.assertEqual(count_request.count(), 1)

        first_request = count_request[0]
        self.assertEqual(first_request.request_list, 'johnny01')

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
        eric_sent_to_stefanie.request.add(request_eric_to_stefanie)'''