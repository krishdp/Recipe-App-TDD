from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create and save a new user."""
        if not email:
            raise ValueError('User must have a email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        
        return user
    
    def create_superuser(self, email, password):
        """Create and save a new superuser."""
        user = self.create_user(email=email, password=password)
        user.is_stuff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that support email insted username."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_stuff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
