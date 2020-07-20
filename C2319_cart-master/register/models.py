from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator , MaxValueValidator

# Create your models here.

JOB = (
    (0,"Undergraduate Student"),
    (1,"Graduate Student"),
    (2,"Faculty Member"),
    (3,"Staff"),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # location = models.CharField(max_length=30, default=0, blank=True, null=True)
    street_address_1 = models.CharField(max_length=30, default='', blank=True, null=True)
    street_address_2 = models.CharField(max_length=30, default='', blank=True, null=True)
    city = models.CharField(max_length=30, default='', blank=True, null=True)
    state = models.CharField(max_length=30, default='', blank=True, null=True)
    zip = models.IntegerField(default='', blank=True, null=True, validators=[MaxValueValidator(100000)])
    age = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(16) , MaxValueValidator(150)])
    occupation = models.IntegerField(choices=JOB , default = 4)
    #first_name = models.CharField(max_length=30, null=False, blank=False)
    #last_name = models.CharField(max_length=150, null=False, blank=False)



    def __str__(self):
        return self.user.username

