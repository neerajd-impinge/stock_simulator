import Decimal


from django.db import models
from django.contrib.auth.models import User




class UserProfile(models.Model):
	user=models.OneToOneField(User)
	available_balance=models.DecimalField(
max_digits=8,decimal_places=2,default= Decimal ( 100000 ) )


# Create your models here.
