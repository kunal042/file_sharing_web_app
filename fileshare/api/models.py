from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission


class User(AbstractUser):
    is_ops_user = models.BooleanField(default=False)
    is_client_user = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='api_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='api_users_permissions', blank=True)


class file(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to = 'media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)



