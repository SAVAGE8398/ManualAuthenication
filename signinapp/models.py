from django.db import models

# Create your models here.
class SignDB(models.Model):
    UserNameF=models.CharField(max_length=122)
    EmailF=models.EmailField(blank=True)
    PasswordF=models.CharField(max_length=122)
    