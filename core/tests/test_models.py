from django.test import TestCase
from core import factories
from core.models import User

class UserModelTest(TestCase):
    def test_user_factory_creation(self):
        user_factory = factories.UserFactory()

        users = User.objects.filter(first_name=user_factory.first_name)

        self.assertEqual(user_factory, users[0])
