from django.test import TestCase
from core import factories
from core.models import User, Category, Task, Group

class UserModelTest(TestCase):
    def test_user_factory_creation(self):
        user_factory = factories.UserFactory()

        users = User.objects.filter(first_name=user_factory.first_name)

        self.assertEqual(user_factory, users[0])


class CategoryModelTest(TestCase):
    def test_category_factory_creation(self):
        category_factory = factories.CategoryFactory()


        categories = Category.objects.filter(name=category_factory.name)


        self.assertEqual(category_factory, categories[0])


class TaskModelTest(TestCase):
    def test_task_factory_creation(self):
        task_factory = factories.TaskFactory()


        tasks = Task.objects.filter(name=task_factory.name)


        self.assertEqual(task_factory, tasks[0])


class TaskModelTest(TestCase):
    def test_group_factory_creation(self):
        group_factory = factories.GroupFactory()


        groups = Group.objects.filter(name=group_factory.name)


        self.assertEqual(group_factory, groups[0])
        