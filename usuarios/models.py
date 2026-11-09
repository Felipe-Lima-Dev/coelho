from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=65)
    password = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username
    
    def __str__(self):
        return self.password
    
    def __str__(self):
        return self.email
