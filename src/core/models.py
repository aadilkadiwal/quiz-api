from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser
from . import managers

class UuidMixin(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid4, editable=False)

    class Meta:
        abstract = True

class TimestampMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)   

    class Meta:
        abstract = True

class AbstractBaseSet(UuidMixin, TimestampMixin):

    class Meta:
        abstract = True

class User(AbstractUser, AbstractBaseSet):
    username = models.CharField(max_length=50, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)        

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    manager = managers.UserManager()

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)