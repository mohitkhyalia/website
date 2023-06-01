from django.db import models

# Create your models here.

class main_ad(models.Model):

    title = models.CharField(max_length=100)
    img=models.CharField(max_length=100)
    dec=models.CharField(max_length=100)

class option(models.Model):

    title = models.CharField(max_length=100)
    img=models.CharField(max_length=100)
    link =models.CharField(max_length=100)

class fb(models.Model):

    name = models.CharField(max_length=100)
    msg=models.CharField(max_length=100)
    mail= models.EmailField( max_length=254)

class foodlist(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    pat = models.CharField(max_length=100)
    dec=models.CharField(max_length=100)