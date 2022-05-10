# Imports
from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import *
from django.template.defaultfilters import slugify

#Add Entitites (as classes) Here:
class User_Data(models.Model):
    email = models.EmailField(unique= True, blank = False)
    username = models.CharField(unique = True, blank = False, max_length=50)
    password = models.CharField(max_length=100) # need to add constraints
    streak = models.IntegerField(default=0)
    award_number = models.IntegerField(default=0)
    first_name = models.CharField(max_length=50, blank = False) # 
    last_name = models.CharField(max_length=50, blank = False)

    # Time will be updated with
    time_worked = models.DecimalField(decimal_places=2) # Time Represented in Hours   
    time_break = models.DecimalField(decimal_places=2) 

    # Meta:
    class Meta:
        app_label = 'app'

    # General Functions
    def __str__(self):
        return "debug output"

    # Model Functions

class User_Rewards(models.Model):
    # Entities:
    email_address = models.ForeignKey(User_Data, on_delete=models.CASCADE)
    award_name = models.CharField(max_length=50)
    award_value = models.IntegerField()

    # Meta:
    class Meta:
        app_label = 'app'

    # General Functions:
    def __str__(self):
        return "debug output"

    # Model Functions:


# Notion Entities
class Notion_DB(models.Model):
    token = models.CharField(max_length=100)
    databaseID = models.CharField(max_length=100)
    # add pageID support as well

    class Meta:
        app_label = 'app'

    def __str__(self):
        return self.databaseID


