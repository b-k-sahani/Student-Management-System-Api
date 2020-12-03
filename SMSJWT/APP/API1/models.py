from django.db import models


# class UserModel(models.Model):
#     class UserSerializer(serializers.Model):
#         password = models.CharField(max_length=50, min_length=6, write_only=True)
#
#     email = models.EmailField(max_length=100)
#     fname = models.CharField(max_length=100)
#     fname = models.CharField(max_length=100)
#     udep = models.CharField(max_length=50)
#     phoneno = models.IntegerField()
#     gender = models.CharField(max_length=100)


import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):   # manager for a custom user model

    def create_user(self, email, password=None):    #Create and return a `User` with an email, username and password.
        if not email:
            raise ValueError('Users Must Have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):    #Create and return a `User` with superuser (admin) permissions.

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        # user.is_superuser = True
        # user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
        )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Shows th dj the UserManager class defined above should manage objects of this type.
    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "login" #making table in database