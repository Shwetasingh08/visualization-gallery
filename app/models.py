from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class feedback(models.Model):
    user = models.CharField(max_length=100)
    feedback_type = models.CharField(max_length=100, choices=(('Code', 'Code'),('Graph', 'Graph'), ('Graph Category', 'Graph Category'), ('Other', 'Other')))
    feedback = models.TextField()

    def _str_(self):
        return self.feedback_type
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    
    def _str_(self):
        return self.name