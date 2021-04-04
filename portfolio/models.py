from django.db import models

# Create your models here.

# Creating Contact Model
class Contact(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email