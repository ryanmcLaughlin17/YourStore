from django.contrib import admin
from .models import Bakery_Item, Sandwiches_and_Prepared_Food, Pastry_Item, Egg_Bite, Porridge_Item
# Register your models here.
admin.site.register(Bakery_Item)
admin.site.register(Sandwiches_and_Prepared_Food)
admin.site.register(Pastry_Item)
admin.site.register(Egg_Bite)
admin.site.register(Porridge_Item)