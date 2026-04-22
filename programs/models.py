from django.db import models

class Program(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
