from django.shortcuts import render
from .models import Bakery_Item, Sandwiches_and_Prepared_Food, Pastry_Item, Egg_Bite, Porridge_Item
# Create your views here.

def food_home(request):
    return render(request, "food/food_home.html")

def sales(request):
    return render(request, 'food/sales.html')

def waste(request):
    return render(request, 'food/waste.html')

def ordering(request):
    return render(request, 'food/ordering.html')

def bakery_item(request):
    bakery_item = Bakery_Item.objects.all().order_by('name')
    return render(request, 'food/sales.html', {'bakery_items':bakery_item})

def sandwiches_and_prepared_food(request):
    sandwiches_and_prepared_food = Sandwiches_and_Prepared_Food.objects.all().order_by('name')
    return render(request, 'food/sales.html', {'sandwiches_and_prepared_food':sandwiches_and_prepared_food})

def pastry_item(request):
    pastry_item = Pastry_Item.objects.all().order_by('name')
    return render(request, 'food/sales.html', {'pastry_item':pastry_item})

def egg_bite(request):
    egg_bite = Egg_Bite.objects.all().order_by('name')
    return render(request, 'food/sales.html', {'egg_bite':egg_bite})

def porridge_item(request):
    porridge_item = Porridge_Item.objects.all().order_by('name')
    return render(request, 'food/sales.html', {'porridge_item':porridge_item})