from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from match.models import human, Subject, Wantmatch, Review, Matched, Chatroomname, Tutor, Student


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
        User.objects.create_user(username='kitsanapong', password='kpassword')
        User.objects.create_user(username='pasakorn', password='mpassword')

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

    def test_cancel_request(self):
        User.objects.create_user(username='kitsanapong', password='kpassword')
        User.objects.create_user(username='pasakorn', password='mpassword')
        pasakornh = human.objects.create(name='pasakorn')
        kitsanapongh = human.objects.create(name='kitsanapong')
        self.client.login(username="kitsanapong", password="kpassword")

        chatname = Chatroomname.objects.create(name='kitsanapong' + 'pasakorn')
        chatname.save()
        chatnamer = Chatroomname.objects.get(name='kitsanapong' + 'pasakorn')
        human.objects.get(name='kitsanapong').chatroomname.add(chatnamer)
        human.objects.get(name='pasakorn').chatroomname.add(chatnamer)

        self.client.post(f'/matching/{pasakornh.name}')

        wmforpasa=pasakornh.wantmatch.filter(name='kitsanapong')
        self.assertEqual(wmforpasa.count(), 1)

        self.client.post(f'/unmatching/{pasakornh.name}')

        wmforpasa=pasakornh.wantmatch.filter(name='kitsanapong')
        self.assertEqual(wmforpasa.count(), 0)


    def test_accept_request(self):
        User.objects.create_user(username='kitsanapong', password='kpassword')
        User.objects.create_user(username='pasakorn', password='mpassword')

        pasakornh = human.objects.create(name='pasakorn')
        kitsanapongh = human.objects.create(name='kitsanapong')

        # kitsanapong login
        self.client.login(username="kitsanapong", password="kpassword")
        chatname = Chatroomname.objects.create(name='kitsanapong' + 'pasakorn')
        chatname.save()
        chatnamer = Chatroomname.objects.get(name='kitsanapong' + 'pasakorn')
        human.objects.get(name='kitsanapong').chatroomname.add(chatnamer)
        human.objects.get(name='pasakorn').chatroomname.add(chatnamer)
        firstwm = Wantmatch.objects.create(name='pasakorn')
        human.objects.get(name='kitsanapong').wantmatch.add(firstwm)
        ttall = Tutor.objects.all()
        self.assertEqual(ttall.count(), 0)
        stall = Student.objects.all()
        self.assertEqual(stall.count(), 0)
        self.client.post(f'/acceptmatch/{pasakornh.name}')
        ttall = Tutor.objects.all()
        self.assertEqual(ttall.count(), 1)
        self.assertEqual(ttall[0].name, 'kitsanapong')
        stall = Student.objects.all()
        self.assertEqual(stall.count(), 1)
        self.assertEqual(stall[0].name, 'pasakorn')

    def test_decline_request(self):
        User.objects.create_user(username='kitsanapong', password='kpassword')
        User.objects.create_user(username='pasakorn', password='mpassword')

        pasakornh = human.objects.create(name='pasakorn')
        kitsanapongh = human.objects.create(name='kitsanapong')

        # kitsanapong login
        self.client.login(username="kitsanapong", password="kpassword")
        chatname = Chatroomname.objects.create(name='kitsanapong' + 'pasakorn')
        chatname.save()
        chatnamer = Chatroomname.objects.get(name='kitsanapong' + 'pasakorn')
        human.objects.get(name='kitsanapong').chatroomname.add(chatnamer)
        human.objects.get(name='pasakorn').chatroomname.add(chatnamer)
        firstwm = Wantmatch.objects.create(name='pasakorn')
        kitsanapongh.wantmatch.add(firstwm)

        allwmfork=human.objects.get(name='kitsanapong').wantmatch.filter(name='pasakorn')
        self.assertEqual(allwmfork.count(), 1)
        human.objects.get(name='kitsanapong').wantmatch.add(firstwm)

        self.client.post(f'/declinematch/{pasakornh.name}')
        allwmfork = human.objects.get(name='kitsanapong').wantmatch.filter(name='pasakorn')
        self.assertEqual(allwmfork.count(),0)

    def test_unmatched(self):
        User.objects.create_user(username='kitsanapong', password='kpassword')
        User.objects.create_user(username='pasakorn', password='mpassword')
        pasakornh = human.objects.create(name='pasakorn')
        kitsanapongh = human.objects.create(name='kitsanapong')

        # kitsanapong login
        self.client.login(username="kitsanapong", password="kpassword")
        chatname = Chatroomname.objects.create(name='kitsanapong' + 'pasakorn')
        chatname.save()
        chatnamer = Chatroomname.objects.get(name='kitsanapong' + 'pasakorn')
        human.objects.get(name='kitsanapong').chatroomname.add(chatnamer)
        human.objects.get(name='pasakorn').chatroomname.add(chatnamer)
        stfirst = Student.objects.create(name='pasakorn')
        kitsanapongh.student.add(stfirst)
        ttfirst = Tutor.objects.create(name='kitsanapong')
        pasakornh.tutor.add(ttfirst)

        allstfork = human.objects.get(name='kitsanapong').student.filter(name='pasakorn')
        self.assertEqual(allstfork.count(), 1)
        allttforp = human.objects.get(name='pasakorn').tutor.filter(name='kitsanapong')
        self.assertEqual(allttforp.count(), 1)

        self.client.post(f'/unmatched/{pasakornh.name}')
        allstfork = human.objects.get(name='kitsanapong').student.filter(name='pasakorn')
        self.assertEqual(allstfork.count(), 0)
        allttforp = human.objects.get(name='pasakorn').tutor.filter(name='kitsanapong')
        self.assertEqual(allttforp.count(), 0)

