
from django.shortcuts import render
# Create your views here.

def food_home(request):
    return render(request, "food/food_home.html")

def sales(request):
    return render(request, 'food/sales.html')

def waste(request):
    return render(request, 'food/waste.html')

def ordering(request):
    return render(request, 'food/ordering.html')