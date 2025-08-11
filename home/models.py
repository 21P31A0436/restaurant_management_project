from django.db import models

# Create your models here.
class Restaurant(models.Models):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name