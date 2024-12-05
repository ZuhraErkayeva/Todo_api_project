from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.CharField(max_length=200)

    def __str__(self):
        return self.title
