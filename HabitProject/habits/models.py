from django.db import models

# Create your models here.

class Habit(models.Model):
#this makes a attribute that describes the individual Habit
#the individual Habit and Value.
    IndHabit=models.TextField()
   
    IndValue=models.IntegerField(default=0)