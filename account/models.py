from django.db import models
from django.conf import settings

class Profile(models.Model):   #profile model that contains all additional fields and a one-to-one relationship with theDjango User model
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	date_of_birth = models.DateField(blank=True, null=True)
	photo = models.ImageField(upload_to='users/%y/%m/%d')
# Create your models here.
