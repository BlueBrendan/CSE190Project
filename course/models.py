from django.db import models

# Create your models here.
class Courses(models.Model):
    name = models.TextField(max_length=16, unique=True)
    title = models.TextField(max_length=256)
    description = models.TextField(max_length=1024)
    units = models.PositiveIntegerField()
    difficulty = models.PositiveIntegerField()
    categories = models.ManyToManyField("category.Category")

    def __str__(self):
        return self.name
