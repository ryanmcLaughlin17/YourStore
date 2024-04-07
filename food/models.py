from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.TextField(max_length=250)
    shelf_life = models.IntegerField()
    type = models.CharField(max_length=25)
    vegan = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)

    def __str__(self):
        return self.name
