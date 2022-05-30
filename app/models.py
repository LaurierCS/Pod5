# Imports
from email.policy import default
# from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import *
from django.template.defaultfilters import slugify

#Add Entitites (as classes) Here:
class User_Data(models.Model):
    # email = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    streak = models.IntegerField(default=0)
    award_number = models.IntegerField(default=0)

    # Time will be updated with
    # time_worked = models.DecimalField(decimal_places=2) # Time Represented in Hours   
    # time_break = models.DecimalField(decimal_places=2) 

    # Meta:
    class Meta:
        app_label = 'app'

    # General Functions
    def __str__(self):
        return self.user.username

    # Model Functions
    # def updateStreak(user_ID, ):


    # def getStats(user_ID):
    #     streak = 


class User_Rewards(models.Model):
    # Entities:
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    award_name = models.CharField(max_length=50)
    award_value = models.IntegerField()

    # Meta:
    class Meta:
        app_label = 'app'

    # General Functions:


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

# Todo:
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    taskID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        app_label = 'app' # mandatory label: declare for all models

    # Set and Get Methods:
    # def completed(taskID):
    #     pass