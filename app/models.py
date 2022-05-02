# Imports
from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import *
from django.template.defaultfilters import slugify

#Add Entitites (as classes) Here:
class User_Login(models.Model):
    # Add Attributes Here:
    email = models.EmailField(unique= True, blank = False)
    password = models.CharField(max_length=100) # need to add constraints

    # Meta:
    class Meta:
        app_label = 'app' # mandatory label: declare for all models

    # Model's General Functions Here:
    def __str__(self):
        return "email: {}, fName: {}, lName: {}".format(self.emailAddress, self.firstName, self.lastName)

    # Model's Classes here:


class User_Data(models.Model):
    email_address = models.OneToOneField( # fk for user
        User,
        on_delete=models.CASCADE, # delete obj if user obj deleted
        primary_key=True
    )
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

class Task_Obj(models.Model):
    databaseID = models.ForeignKey(Notion_DB, on_delete=models.CASCADE)
    taskID = models.CharField(max_length=100)
    date = models.DateTimeField()
    task_title = models.DateTimeField(max_length = 50)
    task_description = models.CharField(max_length = 500)

    class Meta:
        app_label = 'app'

    def __str__(self):
        return self.task_title, 

# Tasks Entities
class Task_Instance(models.Model):
    # Entities:
    task_ID = models.OneToOneField
    task_status = models.BooleanField()
    time_worked = models.IntegerField(default=0)
    time_break = models.IntegerField()#what should the max min for break be and would i put it here
    # ^ int represented in minutes
    #date_worked = models.DateField()

    # Meta:
    class Meta:
        app_label = 'app'

    # General Functions
    def __str__(self):
        return self.task_status
    
class Pomo_Instance(models.Model):
    # Entities:
    task_ID = models.OneToOneField
    pomo_status = models.BooleanField()
    time_elapsed = models.TimeField()

    # Meta:
    class Meta:
        app_label = 'app'
    
    # General Functions
    def __str__(self):
        return self.pomo_status

class Pomo_Settings(models.Model):
    # Entities:
    timer_ID = models.IntegerField()
    email_address = models.EmailField(unique= True, blank = False)
    work_interval = models.PositiveIntegerField
    break_interval = models.PositiveIntegerField
    long_break_interval = models.PositiveIntegerField

    # Meta:
    class Meta:
        app_label = 'app'
    
    #General Functions

class Calender_Obj(models.Model):
    # Entity:
    calender_ID = models.DateTimeField

    # Meta:
    class Meta:
        app_label = 'app'

    # General Functions
    def __str__(self):
        return self.calender_ID

