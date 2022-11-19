from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here. Are the fields of our database
class TaskMate(models.Model):
    # Attaching a task to a user
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    #The task to do
    task = models.CharField(max_length=300)
    #Whether it's done or not
    done = models.BooleanField(default = False)

    # A method to return the actual task name
    def __str__(self):
        return self.task