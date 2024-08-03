from django.db import models
from django.core.validators import MaxValueValidator

class Contact_page_model(models.Model):
    nameform = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    
    #PationtPhysicalActivity = models.BooleanField()
    def __str__(self):
        return f"name :{self.nameform}, Email:{self.email},Subject :{self.subject}, Message:{self.message}"
    

class Newseletter_page(models.Model):
    Email = models.CharField(max_length=60)
    #PationtPhysicalActivity = models.BooleanField()
    def __str__(self):
        return f"Email:{self.Email}"
    