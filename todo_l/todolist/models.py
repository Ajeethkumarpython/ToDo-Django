from django.db import models

# Create your models here.
class Tasks(models.Model):
    task = models.CharField(max_length=1000)
    created_by = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id, self.task
