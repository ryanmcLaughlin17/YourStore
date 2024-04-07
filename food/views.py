from django.shortcuts import render
from .models import Food
# Create your views here.

def food_home(request):
    return render(request, "food/food_home.html")

def sales(request):
    return render(request, 'food/sales.html')

def waste(request):
    return render(request, 'food/waste.html')

def ordering(request):
    return render(request, 'food/ordering.html')

def food(request):
    food = Food.objects.all().order_by('date')
    return render(request, 'food/sales.html', {'food':food})