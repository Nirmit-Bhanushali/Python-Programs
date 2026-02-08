# Defines the data structure for Task Listings
from django.db import models
class TaskListing(models.Model):
    # Fields to hold the task name (String, max length 100)
    title = models.CharField(max_length=100)
    # Field to track if the task is completed (Boolean, default False)
    def __str__(self):
        return self.title