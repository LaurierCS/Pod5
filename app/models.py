# Imports
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import *
from django.template.defaultfilters import slugify

#Add Classes Here:
class User(models.Model):
    # Add Entities Here:
    email_address = models.EmailField(unique= True, blank = False)
    password = models.CharField(widget=forms.PasswordInput) # need to add constraints
    first_name = models.CharField(max_length=50, blank = False) # 
    last_name = models.CharField(max_length=50, blank = False)

    # Meta:
    class Meta:
        app_label = 'app' # mandatory label: declare for all models

    # Model's General Functions Here:
    def __str__(self):
        return "email: {}, fName: {}, lName: {}".format(self.emailAddress, self.firstName, self.lastName)

    # Model's Classes here:


class User_Data(models.Model):
    # Entities:
    email_address = models.OneToOneField( # fk for user
        User,
        on_delete=models.CASCADE, # delete obj if user obj deleted
        primary_key=True
    )
    streak = models.IntegerField(default=0)
    award_number = models.integerField(default=0)

    # Time will be updated form
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
    email_address = models.ForeignKey(User_Data)
    award_name = models.CharField(max_length=50)
    award_value = models.IntegerField()

    # Meta:
    class Meta:
        app_label = 'app'

    # General Functions:
    def __str__(self):
        return "debug output"

    # Model Functions:
    