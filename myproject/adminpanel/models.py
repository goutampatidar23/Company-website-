from django.db import models # type: ignore

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')

class Client(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    designation = models.CharField(max_length=50)
    image = models.ImageField(upload_to='clients/')

class ContactForm(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    city = models.CharField(max_length=50)

class Subscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
