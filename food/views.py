from django.shortcuts import render
from .models import Bakery_Item
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
    bakery_item = Bakery_Item.objects.all().order_by('date')
    return render(request, 'food/sales.html', {'bakery_items':bakery_item})