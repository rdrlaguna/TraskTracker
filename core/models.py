from django.utils import timezone
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, Group, Permission
import uuid

class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False)
    email = models.EmailField(
        unique=True)
    username = models.CharField(
        unique=True,
        max_length=18,
        blank=True,
        null=True)
    first_name = models.CharField(
        max_length=30,
        blank=True)
    last_name = models.CharField(
        max_length=30,
        blank=True)
    is_active = models.BooleanField(
        default=True)
    is_superuser = models.BooleanField(
        default=False)
    date_created = models.DateTimeField(
        default=timezone.now)
    date_updated = models.DateTimeField(
        default=timezone.now)
    last_login = models.DateTimeField(
        default=timezone.now)
    groups = models.ManyToManyField(
        Group,
        verbose_name=("groups"),
        blank=True,
        related_name="users_set",
        related_query_name="users",)
    
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=("user permissions"),
        blank=True,
        help_text=("Specific permissions for this user."),
        related_name="users_set",
        related_query_name="users",
    )
    USERNAME_FIELD="username"
    EMAIL_FIELD="email"

    class Meta : 
        app_label="core"
        db_table="users"
        verbose_name="User"
        verbose_name_plural="Users"

    def __str__(self):
        return f"{self.first_name}, {self.email}"
    

# Category model
class Category(models.Model):
    uuid = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    name = models.CharField(max_length = 64)
    class Meta : 
        app_label="core"
        db_table="categories"
        verbose_name="Category"
        verbose_name_plural="Categories"

    def __str__(self):
        return self.name


# Task model
class Task(models.Model):
    uuid = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    category = models.ForeignKey("core.Category", on_delete=models.CASCADE, related_name="tasks")
    user = models.ManyToManyField("core.User", related_name="tasks")
    name = models.CharField(max_length = 64)
    # started_at = models.DateField()
    # finished_at = models.DateField()
    # created_at = models.DateField()
    class Meta : 
        app_label="core"
        db_table="tasks"
        verbose_name="Task"
        verbose_name_plural="Tasks"

    def __str__(self):
        return self.name



class Group(Group):
    uuid = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    class Meta : 
        app_label="core"
        db_table="groups"
        verbose_name="Group"
        verbose_name_plural="Groups"
