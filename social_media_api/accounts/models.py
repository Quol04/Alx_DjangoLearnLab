from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='accounts_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='accounts_user_permissions',
        blank=True
    )

    def followers_count(self):
        return self.followers.count()
    
    def following_count(self):
        return self.following.count()


    def __str__(self):
        return self.username