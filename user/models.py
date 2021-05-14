from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=100, default="")
    age = models.IntegerField(null=True, blank=True)
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')
    # image = models.FileField()

    def __str__(self):
        return f'{self.user.username} Profile'
