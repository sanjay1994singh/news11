from django.db import models


# Create your models here.
class Follow(models.Model):
    follow = models.BigIntegerField(null=True, blank=True)


class FollowVerify(models.Model):
    email = models.EmailField(unique=True)
    otp = models.IntegerField()
    verify = models.CharField(max_length=10, default='pending')

    def __str__(self):
        return self.email
