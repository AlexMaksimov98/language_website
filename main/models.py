from django.db import models

class User(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class NewUser(models.Model):
    login = models.CharField(max_length=50)
    age = models.IntegerField()
    country = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
