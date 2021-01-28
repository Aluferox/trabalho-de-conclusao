from django.db import models

# Create your models here.

class TasksResults(models.Model):
    id_task = models.CharField(max_length=255)
    result = models.TextField()

    def __str__(self):
        return f'{self.id_task}'