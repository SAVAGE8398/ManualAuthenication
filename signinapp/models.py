from django.db import models

# Create your models here.
class SignDB(models.Model):
    EmailF=models.EmailField(max_length=122)
    PasswordF=models.CharField(max_length=122)
    