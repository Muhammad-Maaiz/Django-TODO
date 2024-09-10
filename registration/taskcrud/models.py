from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=50)
    task_description = models.TextField()
    task_due_date = models.DateField()
    task_created_at = models.DateTimeField(auto_now_add=True)  # Captures creation time
    task_updated_at = models.DateTimeField(auto_now=True)      # Captures update time

