from django.db import models

# Create your models here.

class test(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    location=models.CharField(max_length=20)
    