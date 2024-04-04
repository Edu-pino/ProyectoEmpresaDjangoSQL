from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

    
class Extrafields(models.Model):
    
    # Modelo que representa un registro
    
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    CodCliente = models.IntegerField(default=00000)