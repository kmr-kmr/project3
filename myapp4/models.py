from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Books(models.Model):
    """
    This is Books Model for to dispaly books
    """

    title = models.CharField(max_length = 100)
    pages = models.IntegerField()
    author = models.CharField(max_length = 100)
    pub_date = models.DateField()

    def __str__(self):
        return self.author

class Users(models.Model):
    """
    This is users Model for User registration
    """
    
    name = models.CharField(max_length = 50)
    username = models.CharField(max_length = 50)
    email = models.EmailField()
    password = models.CharField(max_length = 50)
    confirm_password = models.CharField(max_length = 50)
    date_of_birth = models.DateField()
  
    def __str__(self):
        return self.name
