from django.db import models

# class Clients(models.Model):
#   firstname = models.CharField(max_length=255)
#   email = models.EmailField(max_length=254)
#   message = models.TextField()
#   med_aid = models.CharField(max_length=255)
#   med_aid_num = models.IntegerField()

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
