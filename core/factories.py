import factory
from factory import fuzzy
from . import models 



class UserFactory(factory.django.DjangoModelFactory):
    email = fuzzy.FuzzyText(length=10, suffix="@lorem.com")
    username = fuzzy.FuzzyText(length=8, suffix="_uname")
    first_name = fuzzy.FuzzyText(length=10, suffix="_fname")
    last_name = fuzzy.FuzzyText(length=10, suffix="_lname")
    is_active = True
    is_superuser = False

    class Meta : 
        model = models.User
    

# Category model
class CategoryFactory(factory.django.DjangoModelFactory):
    name = fuzzy.FuzzyText(length=20, suffix="_cname")

    class Meta : 
        model = models.Category



# Task model
class TaskFactory(factory.django.DjangoModelFactory):
    category = factory.SubFactory('core.factories.CategoryFactory') 
    user = factory.SubFactory('core.factories.UserFactory')
    name = fuzzy.FuzzyText(length=20, suffix="_tname")

    class Meta :
        model = models.Task
        


class GroupFactory(factory.django.DjangoModelFactory):
    name = fuzzy.FuzzyText(length=20, suffix="_gname")

    class Meta : 
         model = models.Group
