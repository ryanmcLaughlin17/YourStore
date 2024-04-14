from django.db import models

# Create your models here.
class Bakery_Item(models.Model):
    name = models.CharField(max_length=50)
    sku = models.IntegerField(default=0)
    ingredients = models.TextField(max_length=1500)
    vegan = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    time_in_box = models.CharField(max_length=20, default=False)
    time_in_pastry_case = models.CharField(max_length=20, default=False)

    def __str__(self):
        return self.name
