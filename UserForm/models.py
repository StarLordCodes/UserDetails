from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    role = models.CharField(max_length = 15)
    country = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    mobile = models.CharField(max_length=10)
    password = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.name
