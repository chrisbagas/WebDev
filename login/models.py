from multiprocessing import Manager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, full_name,username,password):
        if not full_name:
            raise ValueError("Users must have a full name")
        if not username:
            raise ValueError("Users must have a username")
        if not password:
            raise ValueError("Users must have a password")
        
        user = self.model(
            full_name=full_name,
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user 
    def create_superuser(self, full_name, username,password):
        user = self.create_user(
            username=username,
            full_name=full_name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class Account(AbstractBaseUser):
    full_name = models.CharField(max_length=60)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name']

    objects = MyAccountManager()
    def __str__(self) :
        return self.full_name
    
    def has_perm(self, perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

