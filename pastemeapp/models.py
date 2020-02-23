from django.db import models

# Create your models here.

class pasterDB(models.Model):
    textss_field = models.TextField()
    namess = models.CharField(max_length=20,default="")
