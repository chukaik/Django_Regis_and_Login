from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        #extra_fields.setdefault('username', email)  # If username is required
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)

class myUsers(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    username = None  # Remove username field from AbstractUser
    USERNAME_FIELD = 'email'  # Use email to log in
    REQUIRED_FIELDS = ['name']  # Required when creating superuser

    objects = MyUserManager()

    def __str__(self):
        return self.email
