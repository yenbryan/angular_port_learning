from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rfw import settings


class User(AbstractUser):
    about = models.TextField(null=True)

    def __unicode__(self):
        return u"{}".format(self.username)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

class Project(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()
    owner = models.ForeignKey(User, related_name="project")
    follower = models.ManyToManyField(User, related_name="followed_project", null=True, blank=True)

    def __unicode__(self):
        return self.title
