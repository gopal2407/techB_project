from django.db import models


# Create your models here.
class Task(models.Model):
    CHOICE = [('YES', 'YES'), ('NO', 'NO')]
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    completed = models.CharField(max_length=30)
