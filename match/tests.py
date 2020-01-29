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
