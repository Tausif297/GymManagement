from django.db import models

# Create your models here.
class Plans(models.Model):
    plan_name = models.CharField(max_length=255)
    plan_price = models.IntegerField()
    plan_desc = models.CharField(max_length=255)
    plan_slogan = models.CharField(max_length=255)

class Contact(models.Model):
    name=models.CharField(max_length=255)
    number=models.IntegerField()
    message=models.CharField(max_length=550)

class Member(models.Model):
    username = models.CharField(max_length=255)
    contact_1 = models.IntegerField()
    contact_2 = models.IntegerField()
    email = models.EmailField()
    plans = models.CharField(max_length=200)