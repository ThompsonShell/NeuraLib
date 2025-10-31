from django.db import models
from django.db.models import IntegerChoices
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.timezone import now


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username and email:
            raise ValueError("username and email are require")
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user = self.model(username=username, email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        user = self.create_user(username, email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    class Role(IntegerChoices):
        ADMIN = (1, "admin")
        AUTHOR = (2, "author")
        STUDENT = (3, "student")

    class AuthorType(IntegerChoices):
        PERSONAL = 1
        COMMUNITY = 2

    username = models.CharField(max_length=50)
    email = models.EmailField()
    photo = models.ImageField(upload_to="users/%Y/%m/%d", blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    role = models.IntegerField(choices=Role, default=3)
    date_joined = models.DateTimeField(default=now)


objects = UserManager()
USERNAME_FIELD = 'username'
REQUIRED_FIELDS = ['username', 'email']

UserModel = CustomUser
